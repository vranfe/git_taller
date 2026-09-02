# Cuadrícula Interactiva de Círculos

Aplicación de consola en Python que representa una cuadrícula de 8×8 círculos.
Cada círculo inicia **transparente** (`○`) y cambia a **relleno** (`●`) cuando
el usuario selecciona su coordenada `(X,Y)`.

## Requisitos

- Python 3.8 o superior (no requiere librerías externas).

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/vranfe/git_taller
   cd circle-grid
   ```
2. No se necesita instalar dependencias adicionales.
3. También se puede ejecutar en compilador online, debe ser de Python.

## Ejecución

```bash
python3 main.py
```

## Uso

Al iniciar, el programa muestra la cuadrícula vacía y un menú con 5 opciones:

1. **Mostrar cuadrícula**: imprime el estado actual.
2. **Seleccionar coordenada**: pide `X` (columna) y `Y` (fila), valida que
   estén dentro del rango `[1,8]` y rellena el círculo correspondiente.
3. **Ver coordenadas seleccionadas**: lista el historial de coordenadas
   elegidas hasta el momento.
4. **Reiniciar cuadrícula**: vuelve todos los círculos a transparente y
   borra el historial.
5. **Salir**: termina el programa.

### Ejemplo

```
Elige una opción (1-5): 2
Ingresa la coordenada que deseas seleccionar (formato X,Y).
  Coordenada X (columna): 3
  Coordenada Y (fila): 5
  ✓ Círculo en (3,5) cambiado a estado relleno.
```

## Estructura del proyecto

```
circle-grid/
├── main.py       # Código fuente de la aplicación
└── README.md     # Este archivo
```
