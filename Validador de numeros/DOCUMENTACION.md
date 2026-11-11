# Documentación del Proyecto: Validador de Números

**Materia / Actividad:** Actividad Individual (90 minutos)  
**Título:** Validador de Números  
**Objetivo:** Desarrollar un programa que identifique si un número ingresado es par, impar, positivo, negativo o cero, garantizando una ejecución inmediata sin necesidad de instalar dependencias ni configuraciones complejas.

---

## 📌 Comparativa: ¿Es mejor un archivo `.exe` o un Sitio Web (`.html`)?

| Característica | Aplicativo Web Local (`.html`) | Archivo Ejecutable (`.exe`) |
| :--- | :--- | :--- |
| **Instalación requerida** | **Ninguna**. Abre en cualquier navegador preinstalado (Edge, Chrome). | Ninguna (si está compilado), pero requiere el runtime adecuado. |
| **Seguridad y Antivirus** | **100% seguro**. No activa alarmas de Windows Defender ni SmartScreen. | **Problemático**. Windows suele bloquear archivos `.exe` desconocidos o sin firma digital ("Windows protegió su PC"). |
| **Experiencia visual** | Interfaz moderna, limpia, con colores, tarjetas y botones interactivos. | Ventana de consola de comandos clásica en blanco y negro (o fondo oscuro). |
| **Compatibilidad** | Funciona en Windows, Mac, Linux, tablets y teléfonos móviles. | Solo funciona en el sistema operativo para el que se compiló (Windows). |
| **Veredicto** | 🏆 **La mejor opción con diferencia.** Doble clic y listo. | Útil si el profesor exige estrictamente un archivo de consola. |

> **Nota:** Para tu tranquilidad y cumplimiento total, en este proyecto se entregan **ambas opciones listas para usar**:
> 1. `validador.html`: Aplicativo visual e interactivo para abrir en 1 segundo con doble clic.
> 2. `iniciar_consola.bat` / `validador.ps1`: Versión de consola nativa de Windows.

---

## 🕒 Distribución del Tiempo de Trabajo (Total: 90 minutos)

```mermaid
gantt
    title Cronograma de Trabajo (90 minutos)
    dateFormat  mm
    axisFormat  %M m
    section Fases
    1. Comprensión (10 min) :active, 00, 10m
    2. Diseño (15 min)      :00, 15m
    3. Desarrollo (40 min)  :00, 40m
    4. Pruebas (15 min)     :00, 15m
    5. Entrega (10 min)     :00, 10m
```

---

## Etapa 1: Comprensión (10 min)
*Lectura del problema y análisis de requerimientos.*

### 1.1 Planteamiento del Problema
Se solicita construir un programa que reciba un número por parte del usuario y determine de forma automática y precisa dos características fundamentales:
1. **Su signo:** Si es **positivo**, **negativo** o **cero**.
2. **Su paridad:** Si es **par** o **impar**.

### 1.2 Reglas Matemáticas en Lenguaje Cotidiano
Para que el programa razone correctamente, se aplican las siguientes reglas básicas de la matemática:
* **El Signo:**
  * Si el número es **mayor que 0** ($> 0$), es un número **positivo**.
  * Si el número es **menor que 0** ($< 0$), es un número **negativo**.
  * Si el número es **igual a 0** ($= 0$), es el número **cero**, el cual es un número neutro (no tiene signo ni positivo ni negativo).
* **La Paridad:**
  * Un número es **par** si al dividirlo entre $2$, la división es exacta, es decir, el residuo (resto) es $0$.
  * Un número es **impar** si al dividirlo entre $2$, la división deja un residuo de $1$ (o $-1$ en caso de negativos).
  * **Dato clave sobre el cero:** El número $0$ es formalmente un número **par**, porque $0 \div 2 = 0$ con residuo exacto de $0$.

### 1.3 Requerimientos del Sistema
* **Requerimientos Funcionales:**
  * Permitir que el usuario escriba cualquier número.
  * Comprobar que lo escrito sea efectivamente un número y no letras o símbolos inválidos.
  * Mostrar claramente en pantalla el resultado del signo y de la paridad.
  * Permitir realizar múltiples consultas sin que el programa se cierre inesperadamente.
* **Requerimientos No Funcionales:**
  * **Cero dependencias:** No requerir la instalación de Python, Node.js ni librerías adicionales.
  * **Rapidez de arranque:** Debe abrir y responder de manera instantánea.
  * **Facilidad de uso:** Interfaz intuitiva y mensajes comprensibles para cualquier persona.

---

## Etapa 2: Diseño (15 min)
*Elaboración del algoritmo, pseudocódigo y diagrama de flujo.*

### 2.1 Algoritmo en Lenguaje Natural (Paso a Paso)
1. **Inicio del programa.**
2. **Solicitar el número:** Pedir al usuario que ingrese un valor.
3. **Validación:**
   * Si el usuario no escribió un número válido, mostrar un mensaje de error y pedirlo de nuevo.
4. **Evaluar Signo:**
   * Si el número es mayor a cero $\rightarrow$ Marcar como **Positivo**.
   * Si el número es menor a cero $\rightarrow$ Marcar como **Negativo**.
   * Si el número es igual a cero $\rightarrow$ Marcar como **Cero (Neutro)**.
5. **Evaluar Paridad:**
   * Calcular el residuo de dividir el número entre 2 (operación módulo `%`).
   * Si el residuo es cero $\rightarrow$ Marcar como **Par**.
   * Si el residuo es distinto de cero $\rightarrow$ Marcar como **Impar**.
6. **Mostrar Resultados:** Presentar al usuario los resultados de forma clara.
7. **Repetir o Salir:** Permitir ingresar otro número o cerrar el programa.
8. **Fin del programa.**

### 2.2 Pseudocódigo

```text
Algoritmo ValidadorDeNumeros
    Definir numero Como Real
    Definir signo Como Texto
    Definir paridad Como Texto

    Escribir "Ingrese un número:"
    Leer entrada

    Si entrada NO ES NUMERO Entonces
        Escribir "Error: El dato ingresado no es un número válido."
    Sino
        numero = ConvertirANumero(entrada)

        // 1. Determinar el signo
        Si numero > 0 Entonces
            signo = "Positivo"
        Sino Si numero < 0 Entonces
            signo = "Negativo"
        Sino
            signo = "Cero (Neutro)"
        FinSi

        // 2. Determinar la paridad
        Si (numero % 2 == 0) Entonces
            paridad = "Par"
        Sino
            paridad = "Impar"
        FinSi

        // 3. Salida de resultados
        Escribir "El número ingresado es: ", numero
        Escribir "Signo: ", signo
        Escribir "Paridad: ", paridad
    FinSi
FinAlgoritmo
```

### 2.3 Diagrama de Flujo

```mermaid
flowchart TD
    A([Inicio]) --> B[/Usuario ingresa un número/]
    B --> C{¿Es un número válido?}
    C -- No --> D[Mostrar mensaje de error]
    D --> B
    C -- Sí --> E{¿El número es > 0, < 0 o = 0?}
    
    E -- Número > 0 --> F[Signo = Positivo]
    E -- Número < 0 --> G[Signo = Negativo]
    E -- Número = 0 --> H[Signo = Cero / Neutro]
    
    F --> I{¿El número dividido entre 2 da residuo 0?}
    G --> I
    H --> I
    
    I -- Sí --> J[Paridad = Par]
    I -- No --> K[Paridad = Impar]
    
    J --> L[/Mostrar resultados en pantalla/]
    K --> L
    L --> M{¿Desea ingresar otro número?}
    M -- Sí --> B
    M -- No --> N([Fin])
```

---

## Etapa 3: Desarrollo (40 min)
*Construcción del programa funcional.*

Se desarrollaron dos versiones funcionales para dar la máxima flexibilidad:

### 3.1 Versión Principal: Aplicación Web Local (`validador.html`)
Esta es la versión recomendada por excelencia. Está construida en un único archivo autónomo con **HTML5, CSS3 y JavaScript puro**.
* **Ventaja:** Solo se requiere hacer doble clic sobre el archivo para que se abra en el navegador por defecto (Edge, Chrome, etc.). No requiere conexión a internet ni servidores.
* **Componentes clave del código:**
  1. **Cálculo del módulo (`num % 2`):** Determina con precisión si el número es par o impar.
  2. **Comparaciones de signo (`num > 0`, `num < 0`, `num === 0`):** Establecen la naturaleza del signo.
  3. **Tarjetas visuales con código de colores:**
     * Verde para números positivos.
     * Rojo para números negativos.
     * Azul/Gris para el cero.
  4. **Historial de consultas:** Almacena temporalmente las últimas validaciones para facilitar la revisión del docente o usuario.
  5. **Botones de prueba rápida:** Permiten probar con un solo clic los valores clave (0, 14, -7, -22, 9).

### 3.2 Versión Consola de Windows (`iniciar_consola.bat` / `validador.ps1`)
Para quienes prefieren la experiencia clásica de terminal o si la rúbrica evalúa ejecución por consola de comandos:
* Se ejecuta con doble clic en `iniciar_consola.bat`.
* Utiliza el motor nativo de PowerShell que viene preinstalado en todas las computadoras con Windows 10 y 11.
* No requiere instalar Python ni ningún software externo.

---

## Etapa 4: Pruebas (15 min)
*Validación de operaciones, casos límite y corrección de errores.*

Se elaboró una matriz de pruebas cubriendo todos los casos posibles (positivos, negativos, cero, números grandes y entradas no numéricas):

| ID | Valor Ingresado | Resultado Esperado | Resultado Obtenido | Estado |
| :---: | :---: | :--- | :--- | :---: |
| **P-01** | `14` | Positivo y Par | Positivo (+) y Par | ✅ Exitoso |
| **P-02** | `9` | Positivo e Impar | Positivo (+) e Impar | ✅ Exitoso |
| **P-03** | `-22` | Negativo y Par | Negativo (-) y Par | ✅ Exitoso |
| **P-04** | `-7` | Negativo e Impar | Negativo (-) e Impar | ✅ Exitoso |
| **P-05** | `0` | Cero (Neutro) y Par | Cero (0) y Par | ✅ Exitoso |
| **P-06** | `1000000` | Positivo y Par | Positivo (+) y Par | ✅ Exitoso |
| **P-07** | `abc` | Mensaje de advertencia o bloqueo de entrada | Bloqueado / Mensaje de error amigable | ✅ Exitoso |
| **P-08** | *(vacío)* | No procesar y solicitar entrada | No procesa hasta ingresar dato | ✅ Exitoso |

### Errores Detectados y Corregidos durante el Desarrollo:
1. **Dilema del número 0:** En un borrador inicial se consideraba únicamente "positivo o negativo", lo que dejaba al 0 clasificado erróneamente como par positivo o sin clasificar. Se implementó una condición específica para el cero, aclarando que es un valor **neutro** (sin signo) y matemáticamente **par**.
2. **Prevención de caracteres no numéricos:** El formulario HTML se configuró con `type="number"` y validación de JavaScript con `isNaN()`, evitando que el usuario ingrese texto por accidente.
3. **Manejo de números negativos impares:** En algunos lenguajes, la operación `-7 % 2` retorna `-1` en lugar de `1`. La lógica se ajustó para verificar si el resto es `0` (par) o distinto de cero (impar), garantizando exactitud matemática.

---

## Etapa 5: Entrega (10 min)
*Presentación, demostración y entrega del código.*

### 5.1 Ubicación de los Archivos en tu Computadora
La carpeta del proyecto se encuentra en:  
`C:\Users\CIRA412\.gemini\antigravity\scratch\validador-numeros\`

Contenido de la carpeta:
* 📄 **`validador.html`**: El aplicativo web visual (solo dale doble clic para abrir en Edge/Chrome).
* ⚙️ **`iniciar_consola.bat`**: Ejecutable de consola de Windows (doble clic para abrir en la terminal).
* 📜 **`validador.ps1`**: Código fuente para PowerShell.
* 📝 **`DOCUMENTACION.md`**: Este informe completo con las 5 etapas documentadas.

### 5.2 Cómo Demostrar el Funcionamiento (Paso a Paso)
1. Ve a la carpeta `validador-numeros`.
2. Haz **doble clic** sobre el archivo **`validador.html`**.
3. Se abrirá automáticamente tu navegador habitual.
4. Puedes hacer clic en cualquiera de los botones de **"Pruebas rápidas"** (por ejemplo, el botón `0` o `-7`) o escribir cualquier número en la caja de texto y presionar **"Validar"**.
5. Observa cómo aparecen las insignias de colores con el Signo, la Paridad y la explicación en lenguaje claro, además de guardarse en el historial de la pantalla.

---
*Trabajo individual completado satisfactoriamente cumpliendo los 90 minutos y todas las etapas requeridas.*
