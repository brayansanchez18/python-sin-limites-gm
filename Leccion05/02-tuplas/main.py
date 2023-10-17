# a diferencia de una lista una tupla respeta el orden de los elementos y estos no se pueden modificar
# tampoco podemos agregar o eliminar algun elemento

# creamos una tupla
frutas = ('naranja', 'platano', 'sandia')
print(frutas)
# saber el largo
print(len(frutas))
# acceder a un elemento
print(frutas[0])
# navegacion inversa
print(frutas[-1])
# acceder a un rango
print(frutas[0:1])
# recorrer los elementos de una tupla
for fruta in frutas: 
    print(fruta)
# para modificar el valor de un indice en una tupla debemos convertirlo pimero a una lista
# frutas[0] = 'pera' # <- no funciona
frutaslista = list(frutas)
frutaslista[0] = 'pera'
frutas = tuple(frutaslista)
print('\n', frutas)