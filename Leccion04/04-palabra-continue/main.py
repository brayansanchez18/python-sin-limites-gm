# for i in range(6):
#     if i %2 == 0:
#         print(f'valor: {i}')

for i in range(6):
    if i %2 != 0: # si el valor es un numero impar
        continue # salra a la siguiente iteracion
    print(f'valor: {i}')