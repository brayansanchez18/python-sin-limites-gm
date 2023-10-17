# dada la siguiente tupla
# crear una lista que solo incluya los numero menores a 5
tupla = (13,1,8,3,2,5,7,8)

# definie la lista
lista = []

# filtrar los elementos menores a 5
for element in tupla:
    if element < 5:
        lista.append(element)
        
# imprimirmos la lista
print(tupla)
print(lista)