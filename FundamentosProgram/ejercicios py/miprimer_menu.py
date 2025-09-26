print("BIENVENIDO A PYTHON and dungeons")
while True:
    print("###### Menu principal #######")
    print("1.- Iniciar juego.")
    print("2.- Configuracion.")
    print("3.- Salir del juego.")
    op = input("Elija una opción: ")
    if op == "3":
        print("Buenas noches...")
        break
    elif op == "1":
        print("*** Vamos a crear tu personaje ***")
        print("1.- Guerrero.")
        print("2.- Mago.")
        print("3.- Guardabosque.")
        op = input("Elija una opción: ")
        if op == "1":
            print("Creacion de guerrero:")
            while True:
                fuerza = int(input("Ingrese fuerza (15-20): "))
                if fuerza >= 15 and fuerza <= 20:
                    print("Ingreso exitoso")
                    break
                else:
                    print("Zarpao ctm, ingresa un valor entre 15 y 20.")
            
            
    
    elif op == "2":
        print("<<< Menu configuracion >>>")
    else:
        print("Elija una opcion valida por favor.")
    
