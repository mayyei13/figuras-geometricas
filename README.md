# Figuras Geometricas
## Desarrollador
| Apellidos y nombres |
|---------------------|
| Maylit Mendoza      |

# Figuras Geométricas en Python

Este repositorio contiene un módulo que define clases para representar figuras geométricas básicas, como círculos, rectángulos y triángulos. Cada clase está diseñada para calcular propiedades geométricas como el área y el perímetro de las figuras. El objetivo del proyecto es aplicar buenas prácticas de codificación en Python, asegurándose de que el código cumpla con las convenciones establecidas por PEP8 y utilizando herramientas de análisis de código estático, como `pylint`, para identificar y corregir errores.

## 🛠 Cambios Realizados para Corregir Errores

Durante la revisión y análisis del código, se identificaron varios problemas relacionados con el estilo de codificación, el formato y la documentación del código, que se corrigieron para mejorar la legibilidad, la mantenibilidad y el cumplimiento de las recomendaciones de PEP8. A continuación se detallan los cambios realizados para corregir los errores señalados por la herramienta `pylint`:

1. **Añadido Docstring al Módulo (`missing-module-docstring`)**:
   - **Problema**: El archivo de código no contenía un docstring al inicio del módulo, lo que es una práctica recomendada en Python. El docstring del módulo debe explicar brevemente su propósito y funcionalidad.
   - **Solución**: Se añadió un docstring al principio del archivo `figura_geometrica.py` que explica el propósito del módulo, el cual es representar figuras geométricas básicas y calcular sus propiedades. Este cambio mejora la legibilidad y la comprensión general del código.

2. **Renombrado del Archivo para Cumplir con la Convención `snake_case` (`invalid-name`)**:
   - **Problema**: El nombre del archivo `FiguraGeometrica.py` no seguía la convención de nombrado recomendada por PEP8, que establece que los nombres de los archivos deben utilizar `snake_case`, es decir, minúsculas y palabras separadas por guiones bajos.
   - **Solución**: El archivo fue renombrado a `figura_geometrica.py` para adherirse a esta convención y mejorar la consistencia del proyecto.

3. **Eliminación del `pass` Innecesario en Clases Vacías (`unnecessary-pass`)**:
   - **Problema**: Se encontraron clases que contenían un `pass` innecesario, lo que puede ser considerado como un error de estilo en Python. El `pass` es utilizado para indicar que no se implementa ningún código en ese lugar, pero si una clase no tiene métodos o atributos, el `pass` no es necesario.
   - **Solución**: Se eliminó el `pass` de las clases vacías, limpiando el código y evitando redundancias innecesarias.

4. **Adición de Métodos en las Clases para Evitar el Error "Demasiados Pocos Métodos Públicos" (`too-few-public-methods`)**:
   - **Problema**: Algunas clases contenían solo uno o dos métodos públicos, lo que puede dificultar la expansión del código o hacer que se considere mal diseñado. Pylint recomendó que las clases tuvieran más métodos públicos para mejorar su estructura.
   - **Solución**: Se añadieron métodos relevantes en las clases para asegurar que cada clase tuviera una funcionalidad adecuada y suficiente. Por ejemplo, se añadieron métodos adicionales para obtener los nombres de las figuras o realizar cálculos adicionales, lo que mejora la funcionalidad general de las clases.

5. **Añadidos Docstrings en las Clases (`missing-class-docstring`)**:
   - **Problema**: Las clases no contaban con docstrings que describieran su propósito o la funcionalidad de sus métodos. El código sin documentación es más difícil de mantener y entender por otros desarrolladores.
   - **Solución**: Se añadieron docstrings a todas las clases para explicar su propósito y lo que hacen, lo que facilita la comprensión del código y mejora su legibilidad.

6. **Eliminación de Clases con Pocos Métodos Públicos (`too-few-public-methods`)**:
   - **Problema**: Se identificaron varias clases con solo uno o dos métodos públicos, lo que puede indicar un diseño de clases deficiente o mal estructurado.
   - **Solución**: Se añadieron más métodos y se reestructuraron algunas clases para hacerlas más completas, con el fin de evitar que tengan menos de dos métodos públicos. Esto mejora la funcionalidad y la coherencia del código.

7. **Añadidos Espacios Consistentes en las Expresiones y Operadores (`C0103`)**:
   - **Problema**: El código original no tenía un formato consistente en cuanto a los espacios alrededor de los operadores, lo que afectaba la legibilidad. Según las directrices de PEP8, se debe dejar un espacio alrededor de los operadores de asignación y aritméticos.
   - **Solución**: Se corrigieron los espacios alrededor de los operadores para que el código sea más legible y siga las mejores prácticas de estilo.

8. **Otros Ajustes Menores en el Formato**:
   - **Problema**: El código original tenía algunos problemas de formato, como espacios inconsistentes entre operadores y líneas, y uso incorrecto de la indentación en algunos casos.
   - **Solución**: Se realizaron ajustes en el espaciado, la indentación y el formato de acuerdo con las reglas de PEP8. Esto incluye asegurarse de que haya un espacio alrededor de los operadores y que las líneas no excedan el límite recomendado de 79 caracteres.

![Áreas Geométricas](https://w7.pngwing.com/pngs/153/804/png-transparent-cube-art-geometric-shapes-photography-area-vector-space.png)


