numero = int(input('proporcina un valor entre 1 y 3'))
numerotexto = ''

if numero == 1:
    numerotexto = 'numero uno'
elif numero == 2:
    numerotexto = 'numero dos'
elif numero == 3:
    numerotexto = 'numero tres'
else:
    numerotexto = 'valor fuera de rango'

print(f'numero proporcionado: {numero}: {numerotexto}')