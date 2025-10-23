#Escriba un programa que permita ingresar una frase y entregue el número de palabras que contiene la frase.

frase = input("Ingrese frase: ")

contador = 0
en_palabra = False  

for letra in frase:
    if letra != " " and not en_palabra:
        contador += 1
        en_palabra = True
    elif letra == " ":
        en_palabra = False

print("La frase contiene", contador, "palabras")
