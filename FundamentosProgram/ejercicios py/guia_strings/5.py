
frase = input("Ingrese frase: ")

palabra_actual = ""   
palabra_mayor = ""    

for letra in frase:
    if letra != " ":
        palabra_actual += letra  
    else:
        if len(palabra_actual) > len(palabra_mayor):
            palabra_mayor = palabra_actual
        palabra_actual = ""

if len(palabra_actual) > len(palabra_mayor):
    palabra_mayor = palabra_actual

print("La palabra con mayor longitud es:", palabra_mayor)
