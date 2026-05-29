# P10 - Gestor de Pedidos

## Problemas detectados
1. **Falta de modularidad en validaciones:** El código de la aplicación requería funciones de validación externas (`validar_nombre` y `validar_email`) que no estaban implementadas en el archivo principal de lógica, rompiendo los tests automatizados.
2. **Desajuste en tramos de descuento:** Los tramos matemáticos de descuento aplicados en la lógica original no coincidían con las expectativas de los asserts de los tests (el test esperaba un 15% para 200€, mientras que el código aplicaba tramos obsoletos).
3. **Malas prácticas de estilo y bugs potenciales:** Presencia de comparaciones redundantes (`while salir == False`), nombres de variables ambiguos (`l` en bucles en lugar de descriptivos) y líneas excesivamente largas que dificultaban la lectura.
4. **Falta de visibilidad de módulos en CI:** El entorno de ejecución de GitHub Actions (Linux) no era capaz de localizar la raíz del proyecto para importar los módulos durante la ejecución de Pytest.

## Refactorizaciones realizadas
| Problema | Refactorización | Archivo | Commit |
|---|---|---|---|
| Funciones de validación ausentes | Implementación de `validar_nombre` con `.strip()` y `validar_email` usando `regex`. | `clientes.py` | "Completa lógica base exigida por los tests" |
| Discrepancia en test de silla de 170€ | Ajuste del tramo en `calcular_descuento` para aplicar 15% a partir de 200€. | `pedidos.py` | "Refactoriza lógica de descuentos" |
| Comparaciones redundantes de booleanos | Reemplazo de `== False` por el operador lógico `not`. | `app.py`, `clientes.py` | "Corrige formato de estilo para Ruff" |
| Nombres de variables ambiguos | Cambio de la variable de bucle `l` por la palabra descriptiva `linea`. | `pedidos.py` | "Corrige formato de estilo para Ruff" |
| Líneas de código excesivamente largas | Formateo e indentación de condiciones de búsqueda y prints en múltiples líneas. | `clientes.py`, `pedidos.py` | "Corrige formato de estilo para Ruff" |

## Pruebas creadas
| Test | Qué comprueba |
|---|---|
| `test_cliente_valido` | Valida que un cliente con datos correctos e ID de teléfono opcional se instancie bien. |
| `test_cliente_con_email_invalido` | Verifica que el método `.es_valido()` devuelva False si el formato del correo es erróneo. |
| `test_validar_nombre_rechaza_vacio` | Comprueba que un nombre compuesto únicamente por espacios en blanco sea rechazado. |
| `test_validar_email_correcto` | Certifica que una dirección con estructura estándar sea aceptada con True. |
| `test_total_final_pedido_con_descuento` | Valida que un subtotal de 200€ aplique correctamente el descuento final esperado de 30€ (quedando en 170€). |
| `test_descuento_exacto_doscientos_euros` | Re-comprueba de forma aislada que la función matemática de tramos responda bien en el límite de los 200€. |

## Analizador de código
Analizador usado: **Ruff**
Opciones configuradas:
1. `line-length = 100`: Restricción de longitud máxima de línea a 100 caracteres para garantizar la legibilidad horizontal.
2. `exclude = [".venv", "__pycache__"]`: Exclusión de entornos virtuales y archivos de caché para optimizar el tiempo de análisis.
3. `select = ["E", "F", "W", "I"]`: Activación de filtros para errores de estilo (E), errores lógicos (F), avisos de diseño (W) y ordenación de bloques de importación (I).

## Trabajo con Git y ramas
* **Rama creada:** `refactor-descuentos`
* **Commits principales:** * `"Refactoriza lógica de descuentos"` (Ajuste de tramos matemáticos y blindaje con tests).
  * `"Corrige formato de estilo para Ruff"` (Solución de los 12 avisos del linter).
  * `"Configura pythonpath para pytest en CI"` (Arreglo de rutas del proyecto).
* **Fusión realizada:** Integración completa de la rama secundaria sobre la rama principal `main` mediante la técnica de avance rápido (*Fast-Forward*).

## Integración continua
* **Resultado del workflow:** **Pipeline en VERDE (Success).** Tras solventar las restricciones iniciales de formato impuestas por Ruff y declarar el `pythonpath = ["."]` dentro de `pyproject.toml` para que Pytest localizara los módulos en Linux, el flujo automatizado compila, analiza y pasa satisfactoriamente los 10 tests del sistema en cada subida de código.


