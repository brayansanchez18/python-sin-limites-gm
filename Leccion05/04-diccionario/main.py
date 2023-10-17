# diccionario llave valor
diccionario = {
    'ide': 'integrated development environment',
    'oop': 'object oriented programming',
    'dbms': 'database management system'
}

print(diccionario)

#largo
print(len(diccionario))
#acceder a un elemento key
print(diccionario['ide'])
# otra forma de recuperar un elemento
print(diccionario.get('oop'))
# modificar un elemento
diccionario['ide'] = 'INTEGRATED DEVELOPMENT ENVIRONMENT'
print(diccionario)
#recorrer los elementos
    
for key, value in diccionario.items():
    print(key, value)

for dicckey in diccionario.values():
    print(dicckey)
    
for termino in diccionario:
    print(termino)
    
for termino in diccionario.keys():
    print(termino)
    
# comprobar la existencia de algun elemento
print('ide' in diccionario)

# agregar un elemento
diccionario['pk'] = 'primary key'
print(diccionario)

# remover un elemento
diccionario.pop('dbms')
print(diccionario)

# limpiar
diccionario.clear()
print(diccionario)