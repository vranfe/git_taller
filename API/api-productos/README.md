# API de Productos

Proyecto académico sencillo de una API REST para administrar productos usando Python y FastAPI.

Los productos se guardan temporalmente en una lista en memoria (no hay base de datos).

## Requisitos

- Python 3.10 o superior

## Crear el entorno virtual

Abre una terminal en la carpeta `api-productos` y ejecuta:

```bash
python -m venv venv
```

## Activar el entorno virtual en Windows

```bash
venv\Scripts\activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar la API con Uvicorn

```bash
uvicorn main:app --reload
```

La API quedará disponible en:

```
http://127.0.0.1:8000
```

## Documentación interactiva (Swagger)

Abre en el navegador:

```
http://127.0.0.1:8000/docs
```

Desde Swagger puedes probar todos los endpoints sin usar otra herramienta.

## Endpoints disponibles

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/productos` | Consultar todos los productos |
| GET | `/productos/{id}` | Consultar un producto por ID |
| POST | `/productos` | Registrar un producto nuevo |
| PUT | `/productos/{id}` | Actualizar un producto existente |
| DELETE | `/productos/{id}` | Eliminar un producto |

## Campos del producto

- `id`: entero (único)
- `nombre`: texto (obligatorio)
- `categoria`: texto
- `precio`: número decimal (debe ser mayor que cero)
- `stock`: entero (no puede ser negativo)

## Ejemplo de producto (JSON)

```json
{
  "id": 1,
  "nombre": "Teclado mecánico",
  "categoria": "Periféricos",
  "precio": 89900.50,
  "stock": 15
}
```
