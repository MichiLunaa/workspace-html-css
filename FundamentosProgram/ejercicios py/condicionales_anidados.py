dia = "Lunes"
hora = 14
'''
if dia == "Lunes" or dia == "Martes":
    if hora < 13:
        print("Es horario de clases")
    else:
        print("Es hora de almuerzo")
else:
    print("No es lunes ni martes")
'''

if (dia == "Lunes" or dia == "Martes") and hora < 13:
    print("Es horario de clases")
elif (dia == "Lunes" or dia == "Martes") and hora >= 13:
    print("Es hora de almuerzo")
else:
    print("No es lunes ni martes")