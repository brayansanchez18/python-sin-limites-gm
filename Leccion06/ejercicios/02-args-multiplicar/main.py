"""
crear una funcion para multiplicar los valores resividos de tipo numerico, utilizando argumentos variables
*args como parametros de la funcion y regresar como resultado la multiplicacion de todos los valores
pasados como argumento
"""

def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

print(multiplicar_valores(3,5,15,3))