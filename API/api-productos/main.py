from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="API de Productos",
    description="API REST académica para administrar productos en memoria.",
    version="1.0.0",
)

# Lista en memoria para simular el almacenamiento temporal de datos
productos: List[dict] = []


# ==============================================================================
# MODELOS DE DATOS (PYDANTIC)
# ==============================================================================

class Producto(BaseModel):
    id: int
    # [MEJORA 2 - ERROR IDENTIFICADO: Validación incompleta de cadenas vacías]
    # Se agrega min_length=1 para asegurar que el texto no esté vacío ni sea una cadena nula
    nombre: str = Field(min_length=1, description="Nombre obligatorio del producto (no vacío)")
    categoria: str = Field(min_length=1, description="Categoría obligatoria del producto (no vacía)")
    precio: float = Field(gt=0, description="El precio debe ser estrictamente mayor que cero")
    stock: int = Field(ge=0, description="El stock no puede ser un número negativo")


class ProductoActualizar(BaseModel):
    # [MEJORA 2 - ERROR IDENTIFICADO: Validación incompleta de cadenas vacías]
    # Se replica la validación min_length=1 en el modelo de actualización
    nombre: str = Field(min_length=1, description="Nombre obligatorio del producto (no vacío)")
    categoria: str = Field(min_length=1, description="Categoría obligatoria del producto (no vacía)")
    precio: float = Field(gt=0, description="El precio debe ser estrictamente mayor que cero")
    stock: int = Field(ge=0, description="El stock no puede ser un número negativo")


# ==============================================================================
# FUNCIONES AUXILIARES
# ==============================================================================

def buscar_producto_por_id(id_producto: int):
    for producto in productos:
        if producto["id"] == id_producto:
            return producto
    return None


# ==============================================================================
# ENDPOINTS (RUTAS DE LA API)
# ==============================================================================

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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return producto


@app.post(
    "/productos",
    response_model=Producto,
    # [MEJORA 1 - ERROR IDENTIFICADO: Código de estado HTTP por defecto 200 en creación]
    # Según el estándar REST, la creación exitosa de un recurso debe responder con HTTP 201 (Created)
    status_code=status.HTTP_201_CREATED,
    summary="Registrar un producto nuevo",
    description=(
        "Crea un producto y lo guarda en la lista en memoria. "
        "El ID debe ser único. Los campos nombre, categoria, precio y stock son validados automáticamente."
    ),
)
def crear_producto(producto: Producto):
    # [MEJORA 4 - ERROR IDENTIFICADO: Código de error no semántico para colisión de identificadores]
    # Se usa HTTP 409 Conflict en lugar de un 400 genérico cuando el ID ya existe en el sistema
    if buscar_producto_por_id(producto.id) is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Ya existe un producto registrado con el ID {producto.id}"
        )

    nuevo_producto = producto.model_dump()
    productos.append(nuevo_producto)
    return nuevo_producto


@app.put(
    "/productos/{id_producto}",
    response_model=Producto,
    summary="Actualizar un producto existente",
    # [MEJORA 3 - ERROR IDENTIFICADO: Inconsistencia en la documentación de Swagger]
    # Se agrega la descripción detallada que faltaba en este endpoint
    description="Actualiza todos los campos de un producto existente identificado por su ID.",
)
def actualizar_producto(id_producto: int, datos: ProductoActualizar):
    producto = buscar_producto_por_id(id_producto)
    if producto is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")

    producto["nombre"] = datos.nombre
    producto["categoria"] = datos.categoria
    producto["precio"] = datos.precio
    producto["stock"] = datos.stock
    return producto


@app.delete(
    "/productos/{id_producto}",
    response_model=Producto,
    # [MEJORA 3 - ERROR IDENTIFICADO: Inconsistencia en la documentación de Swagger]
    # Se agregan summary y description que estaban completamente ausentes en este endpoint
    summary="Eliminar un producto",
    description="Elimina un producto de la lista en memoria a partir de su ID y devuelve el elemento eliminado.",
)
def eliminar_producto(id_producto: int):
    producto = buscar_producto_por_id(id_producto)
    if producto is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")

    productos.remove(producto)
    return producto
