def contar(palabra):
    palabra = palabra.lower()  
    vocales = 0
    for letra in palabra:
        if letra in "aeiou":
            vocales += 1
    return vocales

def ganador(c1, c2, c3, meta):
    if c1 >= meta and c2 < meta and c3 < meta:
        return 1
    elif c2 >= meta and c1 < meta and c3 < meta:
        return 2
    elif c3 >= meta and c1 < meta and c2 < meta:
        return 3
    else:
        return 0

meta = int(input("Ingrese meta del Juego: "))

c1 = 0
c2 = 0
c3 = 0

while True:
    palabra1 = input("alianza 1: ")
    palabra2 = input("alianza 2: ")
    palabra3 = input("alianza 3: ")

    v1 = contar(palabra1)
    v2 = contar(palabra2)
    v3 = contar(palabra3)

    if v1 > v2 and v1 > v3:
        c1 += 1
    elif v2 > v1 and v2 > v3:
        c2 += 1
    elif v3 > v1 and v3 > v2:
        c3 += 1

    ganador_actual = ganador(c1, c2, c3, meta)
    if ganador_actual != 0:
        print("La alianza ganadora es:", ganador_actual)
        break
