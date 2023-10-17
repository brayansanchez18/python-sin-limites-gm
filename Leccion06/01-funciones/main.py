# definimos la funcion
def mi_funcion(nombre, apellido):
    print('hola mundo des de mi funcin en python')
    print(f'nombre: {nombre}, apellido: {apellido}')
    
mi_funcion('emanuel', 'sanchez')

def sumar(n1, n2):
    return (n1 + n2)

resultado = sumar(5,5)
print(f'resultado suma: {resultado}')

print('-------------------------------------------------')

def o_sumar(a = 0, b = 0):
    return a+b

o_resultado = o_sumar()
print(f'resultado sumar: {o_resultado}')
print(f'resultado sumar: {o_sumar(6, 6)}')
print('-------------------------------------------------')

# argumentos variables
def listarNombres(*nombres): #se antepone el * cuando no sabemos cuantos parametros resivira la funcion
    # y esto lo con vierte en una tupla
    for nombre in nombres:
        print(nombre)
        
listarNombres('monse', 'emanuel', 'sonia', 'alexa')