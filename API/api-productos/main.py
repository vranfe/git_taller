from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="API de Productos",
    description="API REST académica para administrar productos en memoria.",
    version="1.0.0",
)

productos: List[dict] = []


class Producto(BaseModel):
    id: int
    nombre: str
    categoria: str
    precio: float = Field(gt=0, description="Debe ser mayor que cero")
    stock: int = Field(ge=0, description="No puede ser negativo")


class ProductoActualizar(BaseModel):
    nombre: str
    categoria: str
    precio: float = Field(gt=0, description="Debe ser mayor que cero")
    stock: int = Field(ge=0, description="No puede ser negativo")


def buscar_producto_por_id(id_producto: int):
    for producto in productos:
        if producto["id"] == id_producto:
            return producto
    return None


@app.get(
    "/productos",
    response_model=List[Producto],
    summary="Listar todos los productos",
    description="Devuelve la lista completa de productos almacenados en memoria.",
)
def obtener_productos():
    return productos


@app.get(
    "/productos/{id_producto}",
    response_model=Producto,
    summary="Consultar un producto por ID",
    description="Busca un producto específico usando su identificador numérico.",
)
def obtener_producto(id_producto: int):
    producto = buscar_producto_por_id(id_producto)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@app.post(
    "/productos",
    response_model=Producto,
    summary="Registrar un producto nuevo",
    description=(
        "Crea un producto y lo guarda en la lista en memoria. "
        "El ID debe ser único. Los campos nombre, precio y stock se validan automáticamente."
    ),
)
def crear_producto(producto: Producto):
    if buscar_producto_por_id(producto.id) is not None:
        raise HTTPException(status_code=400, detail="ID duplicado")

    nuevo_producto = producto.model_dump()
    productos.append(nuevo_producto)
    return nuevo_producto


@app.put(
    "/productos/{id_producto}",
    response_model=Producto,
    summary="Actualizar un producto",
)
def actualizar_producto(id_producto: int, datos: ProductoActualizar):
    producto = buscar_producto_por_id(id_producto)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    producto["nombre"] = datos.nombre
    producto["categoria"] = datos.categoria
    producto["precio"] = datos.precio
    producto["stock"] = datos.stock
    return producto


@app.delete("/productos/{id_producto}", response_model=Producto)
def eliminar_producto(id_producto: int):
    producto = buscar_producto_por_id(id_producto)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    productos.remove(producto)
    return producto
