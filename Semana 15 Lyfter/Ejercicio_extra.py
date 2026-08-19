# EJERCICIO 1: Suma de Números Naturales
# =============================================================================

def manual_add(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

# Complexity: O(n) (Linear)
# Explanation: Executes a loop 'n' times to perform the sum sequentially.


def add_formula(n):
    return n * (n + 1) // 2

# Complexity: O(1) (Constant)
# Explanation: Performs a fixed set of basic arithmetic operations regardless of 'n'.

"""
RESPUESTAS A PREGUNTAS:
1. ¿Cuál es la complejidad de cada versión?
   - manual_add: O(n) - Lineal.
   - add_formula: O(1) - Constante.

2. ¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?
   - Usaría add_formula (O(1)).
   - Razón: manual_add ejecutaría 1,000,000,000 de iteraciones tardando varios
     segundos o minutos. add_formula usa la fórmula de Gauss y calcula el
     resultado instantáneamente en microsegundos sin consumir CPU innecesaria.
"""


# =============================================================================
# EJERCICIO 2: Linear Search vs Binary Search


def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False

# Complexity: O(n) (Linear)
# Explanation: Scans the array element by element from start to finish in the worst case.


def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Complexity: O(log n) (Logarithmic)
# Explanation: Halves the search space with every iteration.

"""
RESPUESTAS A PREGUNTAS:
1. ¿Cuál es la complejidad de cada algoritmo?
   - linear_search: O(n) - Lineal.
   - binary_search: O(log n) - Logarítmica.

2. ¿En qué condiciones conviene usar cada uno?
   - linear_search: Cuando la lista es pequeña, cuando los datos NO están
     ordenados, o para búsquedas únicas donde no vale la pena ordenar primero.
   - binary_search: Cuando la lista es grande y YA ESTÁ ORDENADA, o cuando se
     van a realizar múltiples búsquedas sobre la misma lista.

3. ¿Qué pasa si la lista no está ordenada?
   - linear_search seguirá funcionando perfectamente.
   - binary_search NO funcionará y retornará resultados incorrectos (falsos negativos),
     ya que asume que el arreglo está ordenado para descartar mitades.
"""

# -----------------------------------------------------------------------------


# =============================================================================
# EJERCICIO 3: print_all_pairs

def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")

# Complexity: O(n^2) (Quadratic)
# Explanation: Contains two nested loops over the same dictionary keys.

"""
RESPUESTAS A PREGUNTAS:
1. ¿Cuál es la complejidad temporal?
   - O(n^2) - Cuadrática (donde 'n' es la cantidad de claves en el diccionario).

2. ¿Cuánto dura si hay 1 millón de claves?
   - Para n = 1,000,000, la cantidad total de impresiones es n^2 = 1,000,000,000,000 (1 billón).
   - Debido al costo del I/O (imprimir en consola) y a ejecutar 1 billón de iteraciones,
     el programa tardaría desde varias horas hasta DÍAS enteros en finalizar.
"""