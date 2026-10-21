# Sistema de Gestión de Inventarios - Persistencia en Java (JDBC y SQLite)

Aplicación de consola en Java que implementa la persistencia de datos mediante **JDBC** y **SQLite**, aplicando el patrón de diseño **DAO (Data Access Object)**.

---

## 📁 Estructura del Proyecto

El proyecto está diseñado de forma directa, sencilla y sin complejidades innecesarias:

```text
gestion_inventario/
├── ConexionDB.java      # Conexión JDBC a SQLite e inicialización de la tabla Producto
├── Producto.java        # Clase modelo (atributos: código, nombre, descripción, precio, cantidad)
├── ProductoDAO.java     # Operaciones CRUD (insertar, listar, buscar por código/nombre, actualizar, eliminar)
├── MenuPrincipal.java   # Interfaz de consola con validación de entradas y opciones para el usuario
├── schema.sql           # Script SQL con la definición de la tabla y datos de prueba
├── ejecutar.bat         # Script para compilar y ejecutar en Windows con un solo clic
├── GUIA_INGLES.md       # Guion sugerido en inglés para el video explicativo (Actividad 6)
└── lib/
    └── sqlite-jdbc-3.45.1.0.jar  # Driver JDBC de SQLite
```

---

## 🛠️ Requerimientos y Tecnologías
- **Lenguaje:** Java (versión 11 o superior).
- **Base de datos:** SQLite (almacenada localmente en el archivo `inventario.db`).
- **Driver JDBC:** SQLite JDBC Driver (`sqlite-jdbc`).

---

## 🚀 Cómo Ejecutar el Proyecto

### Opción 1: En Windows con el archivo `.bat` (Recomendado)
Haz doble clic sobre `ejecutar.bat` o ejecútalo en la terminal:
```cmd
ejecutar.bat
```

### Opción 2: Desde la línea de comandos manual
1. **Compilar:**
   ```bash
   javac -cp "lib/*" *.java
   ```
2. **Ejecutar:**
   ```bash
   java -cp ".;lib/*" MenuPrincipal
   ```

---

## 📋 Funcionalidades Implementadas (Requerimientos)

| Requerimiento | Descripción | Operación CRUD |
| :--- | :--- | :--- |
| **RF1. Registrar productos** | Permite ingresar código único, nombre obligatorio, descripción opcional, precio ($\ge 0$) y cantidad ($\ge 0$). | **Create** |
| **RF2. Consultar productos** | Lista todos los productos o busca individualmente por código o coincidencia en el nombre. | **Read** |
| **RF3. Actualizar productos** | Modifica el precio, la descripción o la cantidad de un producto existente. | **Update** |
| **RF4. Eliminar productos** | Elimina un producto por su código solicitando confirmación obligatoria (S/N). | **Delete** |
| **RF5. Persistir información** | Almacena los registros en `inventario.db` para que se conserven al cerrar y reiniciar el programa. | **Persistencia** |

---

## 🧪 Pruebas Realizadas

1. **Datos válidos:** Inserción exitosa de productos con atributos completos.
2. **Campos vacíos y obligatorios:** Control de código y nombre no vacíos.
3. **Valores incorrectos:** Validación de precios no negativos y cantidades enteras $\ge 0$.
4. **Registros duplicados:** Control de unicidad sobre la clave primaria `codigo`.
5. **Confirmación en eliminación:** Prevención de borrado accidental mediante confirmación explícita del usuario.
6. **Persistencia (Actividad 5):** Verificación de que al salir del programa y volver a iniciarlo, los registros siguen existiendo en el archivo SQLite.
