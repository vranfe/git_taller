
import json
import logging
import os
import sys
import unittest
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field, field_validator

# Configuración
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Products API",
    description="REST API for product management and AI integration.",
    version="1.0.0",
    openapi_tags=[
        {"name": "Products", "description": "Product CRUD operations."},
        {"name": "Artificial Intelligence", "description": "Gemini integration."}
    ]
)

productos = []  # Almacenamiento temporal en memoria.
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_TIMEOUT = 20


# Modelos y validaciones
class Producto(BaseModel):
    id: int = Field(description="Unique product identifier")
    nombre: str = Field(min_length=1, description="Product name")
    categoria: str = Field(min_length=1, description="Product category")
    precio: float = Field(gt=0, description="Price must be positive")
    stock: int = Field(ge=0, description="Stock cannot be negative")

    @field_validator("nombre", "categoria")
    @classmethod
    def validar_texto(cls, valor):
        valor = valor.strip()
        if not valor:
            raise ValueError("This field cannot be empty.")
        return valor


class ProductoActualizar(BaseModel):
    nombre: str = Field(min_length=1)
    categoria: str = Field(min_length=1)
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)

    @field_validator("nombre", "categoria")
    @classmethod
    def validar_texto(cls, valor):
        valor = valor.strip()
        if not valor:
            raise ValueError("This field cannot be empty.")
        return valor


class AIRequest(BaseModel):
    query: str = Field(min_length=1, max_length=2000)
    technique: str = "zero-shot"

    @field_validator("query")
    @classmethod
    def validar_consulta(cls, valor):
        valor = valor.strip()
        if not valor:
            raise ValueError("The query cannot be empty.")
        return valor

    @field_validator("technique")
    @classmethod
    def validar_tecnica(cls, valor):
        valor = valor.strip().lower()
        if valor not in {"zero-shot", "few-shot", "cot"}:
            raise ValueError("Use zero-shot, few-shot or cot.")
        return valor


class AIResponse(BaseModel):
    answer: str
    technique: str
    model: str
    input_tokens: int | None = None
    output_tokens: int | None = None


def buscar_producto(id_producto):
    return next((p for p in productos if p["id"] == id_producto), None)


# CRUD: cinco endpoints
@app.get("/productos", response_model=list[Producto], tags=["Products"],
         summary="List all products")
def obtener_productos():
    return productos


@app.get("/productos/{id_producto}", response_model=Producto,
         tags=["Products"], summary="Get a product by ID")
def obtener_producto(id_producto: int):
    producto = buscar_producto(id_producto)
    if producto is None:
        raise HTTPException(404, "Product not found")
    return producto


@app.post("/productos", response_model=Producto, status_code=201,
          tags=["Products"], summary="Create a product")
def crear_producto(producto: Producto):
    if buscar_producto(producto.id):
        raise HTTPException(409, "Product ID already exists")

    nuevo = producto.model_dump()
    productos.append(nuevo)
    logger.info("Product created: %s", nuevo["id"])
    return nuevo


@app.put("/productos/{id_producto}", response_model=Producto,
         tags=["Products"], summary="Update a product")
def actualizar_producto(id_producto: int, datos: ProductoActualizar):
    producto = buscar_producto(id_producto)
    if producto is None:
        raise HTTPException(404, "Product not found")

    producto.update(datos.model_dump())
    logger.info("Product updated: %s", id_producto)
    return producto


@app.delete("/productos/{id_producto}", response_model=Producto,
            tags=["Products"], summary="Delete a product")
def eliminar_producto(id_producto: int):
    producto = buscar_producto(id_producto)
    if producto is None:
        raise HTTPException(404, "Product not found")

    productos.remove(producto)
    logger.info("Product deleted: %s", id_producto)
    return producto


# Integración con Gemini y técnicas de prompting
def construir_prompt(consulta: AIRequest):
    instrucciones = (
        "You are a product inventory assistant. Answer in Spanish. "
        "Use only the supplied inventory and do not invent information."
    )

    if consulta.technique == "few-shot":
        instrucciones += (
            "\nExample: Question: Is the keyboard available? "
            "Answer: Check the recorded stock before responding."
        )
    elif consulta.technique == "cot":
        instrucciones += (
            "\nAnalyze the available information carefully and provide "
            "a concise answer with a brief justification. Do not reveal "
            "private internal reasoning."
        )

    inventario = json.dumps(productos, ensure_ascii=False)
    return (
        f"{instrucciones}\nInventory: {inventario}"
        f"\nQuestion: {consulta.query}"
    )


def consultar_gemini(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(503, "Gemini API key is not configured.")

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_MODEL}:generateContent?{urlencode({'key': api_key})}"
    )
    cuerpo = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 500}
    }).encode("utf-8")

    peticion = Request(
        url, data=cuerpo,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urlopen(peticion, timeout=GEMINI_TIMEOUT) as respuesta:
            datos = json.loads(respuesta.read().decode("utf-8"))
    except HTTPError as error:
        if error.code == 429:
            raise HTTPException(429, "Gemini rate limit exceeded.")
        logger.error("Gemini HTTP error: %s", error.code)
        raise HTTPException(502, "Gemini provider error.")
    except (TimeoutError, URLError):
        raise HTTPException(504, "Gemini request timed out or failed.")
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise HTTPException(502, "Invalid response from Gemini.")

    try:
        respuesta = datos["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError, TypeError):
        raise HTTPException(502, "Gemini returned no usable answer.")

    uso = datos.get("usageMetadata", {})
    return {
        "answer": respuesta,
        "input_tokens": uso.get("promptTokenCount"),
        "output_tokens": uso.get("candidatesTokenCount")
    }


@app.post("/api/v1/ai", response_model=AIResponse,
          tags=["Artificial Intelligence"],
          summary="Ask Gemini about the product inventory")
def consultar_ia(consulta: AIRequest):
    resultado = consultar_gemini(construir_prompt(consulta))
    logger.info("AI request completed: %s", consulta.technique)
    return {
        **resultado,
        "technique": consulta.technique,
        "model": GEMINI_MODEL
    }


# Tres pruebas de integración
class TestAPI(unittest.TestCase):
    def setUp(self):
        productos.clear()
        self.client = TestClient(app)

    def test_crear_y_consultar(self):
        datos = {
            "id": 1, "nombre": "Teclado",
            "categoria": "Perifericos", "precio": 85000, "stock": 10
        }
        self.assertEqual(self.client.post("/productos", json=datos).status_code, 201)
        respuesta = self.client.get("/productos/1")
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.json()["nombre"], "Teclado")

    def test_id_duplicado(self):
        datos = {
            "id": 2, "nombre": "Mouse",
            "categoria": "Perifericos", "precio": 45000, "stock": 5
        }
        self.client.post("/productos", json=datos)
        self.assertEqual(self.client.post("/productos", json=datos).status_code, 409)

    def test_producto_inexistente(self):
        self.assertEqual(self.client.get("/productos/999").status_code, 404)


if __name__ == "__main__" and "--test" in sys.argv:
    unittest.main(argv=[sys.argv[0]])
