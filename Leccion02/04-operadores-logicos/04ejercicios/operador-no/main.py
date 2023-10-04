# el mismo ejrecicio que el operador or pero invertimos la pregunta
# preguntamos si no son vacaciones o dia de descanso
# significa que tiene deberes por hacer

vacaciones = False
diaDescanso = False

if not (vacaciones or diaDescanso):
    print('Tiene deberes por hacer')
else:
    print('Puede asistir al juego')