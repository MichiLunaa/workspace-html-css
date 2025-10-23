def cuenta_letra(palabra):
    vocales = 0
    consonantes = 0

    for letra in palabra:
        letra = letra.lower()
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            vocales += 1
        elif letra >= "a" and letra <= "z": 
            consonantes += 1
    
    return [vocales, consonantes]

def main():
    palabra = input("Ingrese una palabra: ")
    resultado = cuenta_letra(palabra)
    print(resultado)

main()
