"""
Escuela de Ingeniería Mecatrónica - ITCR
Tarea 1 - Método de selección de operaciones
Estudiantes: Gabriel Alfaro Gómez, Gabriel Araya Álvarez
"""


def operation_selector(num1, num2, op):
    """
    Realiza operaciones (+, -, *, &) con validación de tipos y errores.
    """
    # Validación de enteros (num1 y num2)
    # bool es subclase de int, por eso se debe excluir explícitamente
    if not isinstance(num1, int) or isinstance(num1, bool):
        return -50, None
    if not isinstance(num2, int) or isinstance(num2, bool):
        return -50, None

    # Validación de que 'op' sea string
    if not isinstance(op, str):
        return -60, None

    # Validación de operadores permitidos
    if op not in ["+", "-", "*", "&"]:
        return -70, None

    # Ejecución de la operación
    if op == "+":
        res = num1 + num2
    elif op == "-":
        res = num1 - num2
    elif op == "*":
        res = num1 * num2
    else:  # Caso del operador "&"
        res = num1 & num2

    return 0, res
