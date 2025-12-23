import os  # Error 1: F401 (Importado pero no usado)

def calculo_simple(a,b):
    resultado=a+b  # Error 2: E225 (Faltan espacios alrededor del signo =)
    print("Esta es una linea absurdamente larga que mide mas de setenta y nueve caracteres para forzar el error E501 de flake8")  # Error 3: E501 (Línea muy larga)
    return resultado
