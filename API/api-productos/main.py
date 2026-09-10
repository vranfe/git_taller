import logging
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

# ==============================================================================
# CONFIGURACIÓN DEL SISTEMA DE REGISTRO DE EVENTOS (LOGGING)
# ==============================================================================
# Se configura el módulo estándar logging con el formato requerido:
# Fecha y hora (YYYY-MM-DD HH:MM:SS), Nivel/Tipo de evento (INFO, ERROR) y Mensaje.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("api_productos")

app = FastAPI(
    title="API de Productos",
    description="API REST académica para administrar productos en memoria con registro de eventos (logging).",
    version="1.0.0",
)

# Lista en memoria para simular el almacenamiento temporal de datos
productos: List[dict] = []


# ==============================================================================
# MODELOS DE DATOS (PYDANTIC)
# ==============================================================================

class Producto(BaseModel):
    id: int
    nombre: str = Field(min_length=1, description="Nombre obligatorio del producto (no vacío)")
    categoria: str = Field(min_length=1, description="Categoría obligatoria del producto (no vacía)")
    precio: float = Field(gt=0, description="El precio debe ser estrictamente mayor que cero")
    stock: int = Field(ge=0, description="El stock no puede ser un número negativo")


class ProductoActualizar(BaseModel):
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
# ENDPOINTS (RUTAS DE LA API CON REGISTRO DE EVENTOS)
# ==============================================================================

@app.get(
    "/productos",
    response_model=List[Producto],
    summary="Listar todos los productos",
    description="Devuelve la lista completa de productos almacenados en memoria.",
)
def obtener_productos():
    # Registro de inicio de la petición
    logger.info("GET /productos - Inicio de consulta de productos")
    
    # Registro de operación exitosa
    logger.info(f"GET /productos - Consulta exitosa ({len(productos)} productos encontrados)")
    return productos


@app.get(
    "/productos/{id_producto}",
    response_model=Producto,
    summary="Consultar un producto por ID",
    description="Busca un producto específico usando su identificador numérico.",
)
def obtener_producto(id_producto: int):
    # Registro de recepción de petición
    logger.info(f"GET /productos/{id_producto} - Inicio de búsqueda de producto")
    
    producto = buscar_producto_por_id(id_producto)
    if producto is None:
        # Registro de evento de error
        logger.error(f"GET /productos/{id_producto} - Producto no encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    
    # Registro de operación exitosa
    logger.info(f"GET /productos/{id_producto} - Consulta exitosa")
    return producto


@app.post(
    "/productos",
    response_model=Producto,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar un producto nuevo",
    description=(
        "Crea un producto y lo guarda en la lista en memoria. "
        "El ID debe ser único. Los campos nombre, categoria, precio y stock son validados automáticamente."
    ),
)
def crear_producto(producto: Producto):
    # Registro de recepción de petición con datos
    logger.info(f"POST /productos - Inicio de creación de producto con ID {producto.id}")
    
    if buscar_producto_por_id(producto.id) is not None:
        # Registro de error de conflicto por duplicidad
        logger.error(f"POST /productos - Error: Ya existe un producto con el ID {producto.id}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Ya existe un producto registrado con el ID {producto.id}"
        )

    nuevo_producto = producto.model_dump()
    productos.append(nuevo_producto)
    
    # Registro de operación exitosa
    logger.info(f"POST /productos - Producto registrado exitosamente (ID: {nuevo_producto['id']})")
    return nuevo_producto


@app.put(
    "/productos/{id_producto}",
    response_model=Producto,
    summary="Actualizar un producto existente",
    description="Actualiza todos los campos de un producto existente identificado por su ID.",
)
def actualizar_producto(id_producto: int, datos: ProductoActualizar):
    # Registro de recepción de petición
    logger.info(f"PUT /productos/{id_producto} - Inicio de actualización de producto")
    
    producto = buscar_producto_por_id(id_producto)
    if producto is None:
        # Registro de error si el recurso a actualizar no existe
        logger.error(f"PUT /productos/{id_producto} - Error al actualizar: Producto no encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")

    producto["nombre"] = datos.nombre
    producto["categoria"] = datos.categoria
    producto["precio"] = datos.precio
    producto["stock"] = datos.stock
    
    # Registro de operación exitosa
    logger.info(f"PUT /productos/{id_producto} - Producto actualizado exitosamente")
    return producto


@app.delete(
    "/productos/{id_producto}",
    response_model=Producto,
    summary="Eliminar un producto",
    description="Elimina un producto de la lista en memoria a partir de su ID y devuelve el elemento eliminado.",
)
def eliminar_producto(id_producto: int):
    # Registro de recepción de petición
    logger.info(f"DELETE /productos/{id_producto} - Inicio de eliminación de producto")
    
    producto = buscar_producto_por_id(id_producto)
    if producto is None:
        # Registro de error si el recurso a eliminar no existe
        logger.error(f"DELETE /productos/{id_producto} - Error al eliminar: Producto no encontrado")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")

    productos.remove(producto)
    
    # Registro de operación exitosa
    logger.info(f"DELETE /productos/{id_producto} - Producto eliminado exitosamente")
    return producto
