"""
Escuela de Ingeniería Mecatrónica - ITCR
Tarea 1 - Método de cálculo de promedio
Estudiantes: Gabriel Alfaro Gómez, Gabriel Araya Álvarez
"""


def calculo_promedio(lista_valores):
    """
    Calcula el promedio de una lista con máximo 10 elementos numéricos.
    """
    # Validación de longitud de lista
    if len(lista_valores) > 10:
        return -90, None

    # Validación de elementos numéricos (excluyendo booleanos)
    for i in lista_valores:
        if not isinstance(i, (int, float)) or isinstance(i, bool):
            return -80, None

    # Cálculo del promedio
    resultado = sum(lista_valores) / len(lista_valores)
    return 0, resultado
