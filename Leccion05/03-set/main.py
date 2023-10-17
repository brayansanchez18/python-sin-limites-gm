# lista se pude modificar y mantiene un orden
# tupla, mantiene un orden pero no se puede modificar
# set, no perimite un orden y tampoco permite almacenar elementos duplicados
# no se posible modificar los elementos del set pero si es posible
# agregar elementos o eliminarlos

# definir el set
planetas = {'marte', 'jupiter', 'venus'}
print(planetas)

# saber el largo del set
print(len(planetas))

# revisar si un elemento esta presente
print('marte' in planetas)

#agregar un elemento
planetas.add('tierra')
print(planetas)

# no se pueden duplicar elementos
planetas.add('tierra')
print(planetas)

# eliminar elemento
planetas.remove('tierra')
print(planetas)

# discard sirve para eliminar un elemento si arrojar error en cado de que este
# no se encuentre en el arreglo
planetas.discard('saturno')
print(planetas)

# limpiar los elementos del set
planetas.clear()
print(planetas)

# eliminar todos los elementos del set
del planetas
print(planetas)