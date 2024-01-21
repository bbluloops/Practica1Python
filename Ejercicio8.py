"""Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar."""

hora_usuario = input("Ingrese la hora en formato de 24 horas (hh:mm): ")

# Extraer la hora y los minutos del input del usuario
hora, minutos = map(int, hora_usuario.split(':'))

if 7 <= hora <= 8:
    print("Es la hora del desayuno")
elif 12 <= hora <= 13:
    print("Es la hora del almuerzo")
elif 18 <= hora <= 19:
    print("Es la hora de la cena")
else:
    pass

