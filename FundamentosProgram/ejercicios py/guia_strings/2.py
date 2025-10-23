#Una cadena de ADN es válida si está compuesta únicamente por las bases Adenina (A), Citosina (C), Guanina (G) o Timina (T). Escriba un programa para validar una cadena de ADN. Una cadena de ADN tiene solo 4 caracteres
cadena_adn = input("Ingrese una cadena de ADN: ")
largo = len(cadena_adn)
if largo != 4:
    print("Cadena inválida")
else: 
    for c in cadena_adn:
        if c not in "ACGT":
            print("Cadena inválida")
            validar = False
if validar == True:
    print("Cadena válida")