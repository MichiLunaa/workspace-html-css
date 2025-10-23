def contar(palabra):
    palabra = palabra.lower()     
    vocales = 0
    for letra in palabra:
        if letra in "aeiou":      
            vocales += 1
    return vocales

pal = input("Ingresa una palabra para contar sus vocales: ")
print("Cantidad de vocales:", contar(pal))      

