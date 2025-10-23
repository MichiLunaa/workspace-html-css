# Escriba un programa que permita ingresar una palabra y entregue la cantidad de vocales, consonantes y caracteres especiales.Cualquier otro carácter que no sea vocal ni consonante se considera carácter especial.

palabra = input("Ingrese una palabra: ")
vocales = 0
consonantes = 0
caracteres_especiales = 0
alfabeto = "abcdefghijklmnopqrstuvwxyz"
for letra in palabra:
    letra_min = letra.lower()
    if letra_min in "aeiou":
        vocales += 1
    elif letra_min in alfabeto:
        consonantes += 1
    else:
        caracteres_especiales += 1

print("Cantidad de vocales:", vocales)
print("Cantidad de consonantes:", consonantes)
print("Cantidad de caracteres especiales:", caracteres_especiales)
