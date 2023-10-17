# crear la lista
nombres = ['juan', 'karal', 'ricardo', 'maria']
# imprimir la lista
print(nombres)
# acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])
# acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
# imprimir un rango
print(nombres[0:2]) # sin incluir el indice 2
# ir del inicio de la lista al indice din incluir este ultimo
print(nombres[:3])
# desde el indice indicado hasta el final
print(nombres[1:])
# cambiar el valor de un indice
nombres[3] = 'Ivonne'
print(nombres)
# iterar cadad uno de los elementos de unuestra lista
for nombre in nombres:
    print(nombre)
else:
    print('no existen mas nombres en la lista')
#saber el largo de una lista
print(len(nombres))
# agregar un elemento
nombres.append('lorenzo')
print(nombres)
# insertar un elemento en un indice espesifico
nombres.insert(1, 'octavio')
print(nombres)
# remover un elemento
nombres.remove('octavio')
print(nombres)
# remover el ultimo elemento que se ha agregado a nuestra lista
nombres.pop()
print(nombres)
# eliminar un indice espesifico
del nombres[0]
print(nombres)
# limpiar la lista por completo
nombres.clear()
print(nombres)
#borrar la lsita por completo
del nombres
print(nombres)