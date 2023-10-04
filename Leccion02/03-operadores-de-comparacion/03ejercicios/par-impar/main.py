a = int(input('Escribe un valor numérico: '))

#print(a % 2)
# si divir a % 2 el residuo es = a 0 entonces es un numero par
if a % 2 == 0:
    print(f'El valor de a {a} es número par')
else:
    print(f'El valor de a {a} es número impar')