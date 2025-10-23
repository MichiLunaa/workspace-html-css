def division_correo(correo):
    antes = ""   
    despues = "" 
    encontrado = False  
    
    for letra in correo:
        if letra == "@":
            encontrado = True
        elif not encontrado:
            antes += letra
        else:
            despues += letra
            
    return [antes, despues]

def main():
    correo = input("Ingrese su correo electrónico: ")
    resultado = division_correo(correo)
    print(resultado)

main()
