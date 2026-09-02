
FILAS = 8         
COLUMNAS = 8     
SIMBOLO_VACIO = "○"
SIMBOLO_RELLENO = "●"

def crear_cuadricula(filas, columnas):
    return [[False for _ in range(columnas)] for _ in range(filas)]


def mostrar_cuadricula(cuadricula):
    columnas = len(cuadricula[0])
    filas = len(cuadricula)
    encabezado = "     " + " ".join(f"{c+1:>2}" for c in range(columnas))
    print("\n" + encabezado)
    print("    " + "---" * columnas)


    for y in range(filas):
        fila_str = f"{y+1:>2} | "
        for x in range(columnas):
            simbolo = SIMBOLO_RELLENO if cuadricula[y][x] else SIMBOLO_VACIO
            fila_str += f"{simbolo}  "
        print(fila_str)
    print()


def validar_coordenada(x, y, filas, columnas):

    return 1 <= x <= columnas and 1 <= y <= filas


def seleccionar_circulo(cuadricula, x, y):

    fila_indice = y - 1
    columna_indice = x - 1
    cuadricula[fila_indice][columna_indice] = True


def pedir_entero(mensaje):
   
    while True:
        valor = input(mensaje).strip()
        try:
            return int(valor)
        except ValueError:
            print("  ⚠ Debes ingresar un número entero. Intenta de nuevo.")


def solicitar_coordenada(cuadricula, coordenadas_seleccionadas):
  
    print("\nIngresa la coordenada que deseas seleccionar (formato X,Y).")
    x = pedir_entero("  Coordenada X (columna): ")
    y = pedir_entero("  Coordenada Y (fila): ")

    filas = len(cuadricula)
    columnas = len(cuadricula[0])

    if not validar_coordenada(x, y, filas, columnas):
        print(f"  ✗ Coordenada ({x},{y}) inválida. "
              f"Debe estar entre X:[1,{columnas}] y Y:[1,{filas}].")
        return

    if cuadricula[y - 1][x - 1]:
        print(f"  ℹ La coordenada ({x},{y}) ya estaba seleccionada.")
        return

    seleccionar_circulo(cuadricula, x, y)
    coordenadas_seleccionadas.append((x, y))
    print(f"  ✓ Círculo en ({x},{y}) cambiado a estado relleno.")


def mostrar_seleccionadas(coordenadas_seleccionadas):

    if not coordenadas_seleccionadas:
        print("\nAún no se ha seleccionado ninguna coordenada.")
        return

    print("\nCoordenadas seleccionadas hasta el momento:")
    texto = ", ".join(f"({x},{y})" for x, y in coordenadas_seleccionadas)
    print(f"  {texto}")
    print(f"  Total: {len(coordenadas_seleccionadas)} círculo(s) relleno(s).")


def reiniciar(filas, columnas):
  
    print("\n↺ Cuadrícula reiniciada. Todos los círculos vuelven a transparente.")
    return crear_cuadricula(filas, columnas), []


def mostrar_menu():
    print("=" * 50)
    print(" CUADRÍCULA INTERACTIVA DE CÍRCULOS")
    print("=" * 50)
    print("1. Mostrar cuadrícula")
    print("2. Seleccionar coordenada")
    print("3. Ver coordenadas seleccionadas")
    print("4. Reiniciar cuadrícula")
    print("5. Salir")
    print("-" * 50)


def main():
 
    cuadricula = crear_cuadricula(FILAS, COLUMNAS)
    coordenadas_seleccionadas = []

    mostrar_cuadricula(cuadricula)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            mostrar_cuadricula(cuadricula)

        elif opcion == "2":
            solicitar_coordenada(cuadricula, coordenadas_seleccionadas)
            mostrar_cuadricula(cuadricula)

        elif opcion == "3":
            mostrar_seleccionadas(coordenadas_seleccionadas)

        elif opcion == "4":
            cuadricula, coordenadas_seleccionadas = reiniciar(FILAS, COLUMNAS)
            mostrar_cuadricula(cuadricula)

        elif opcion == "5":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break

        else:
            print("\n⚠ Opción no válida. Elige un número del 1 al 5.")

if __name__ == "__main__":
    main()
