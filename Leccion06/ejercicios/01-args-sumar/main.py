"""
crear una funcion para sumar los valores recibidos de tipo numerico utilizando argumentos variables
*args como parametro de la funcion y regresar como resultado la suma de todos los valores 
pasados como argumento
"""

def sumar(*args):
    for arg in args:
        arg += arg
    return arg

suma = sumar(2,2,2,6)
print(suma)