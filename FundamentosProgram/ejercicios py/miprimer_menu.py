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
                    print("Ingresa un valor entre 15 y 20.")
            while True:
                destreza = int(input("Ingrese destreza (< 20): "))
                if destreza >= 1 and destreza < 20:
                    print("Ingreso exitoso")
                    break
                else:
                    print("Ingresa un valor menor a 20.")
            while True:
                inteligencia = int(input("Ingrese inteligencia (< 20): "))
                if inteligencia >= 1 and inteligencia < 20:
                    print("Ingreso exitoso")
                    break
                else:
                    print("Ingresa un valor menor a 20.")
            suma = fuerza + destreza + inteligencia
            total = suma / 3
            
            while True:
                carisma = int(input("Ingrese carisma (< 20): "))
                if carisma >= 1 and carisma < 20:
                    print("Ingreso exitoso")
                    break
                else:
                    print("Ingresa un valor menor a 20.")

        if op == "2":
            print("Creacion de mago:")
            while True:
                fuerza = int(input("Ingrese fuerza (<12): "))
                if fuerza >= 1 and fuerza < 12:
                    print("Ingreso exitoso")
                    break
                else:
                    print("Ingresa un valor menor a 12.")
            while True: 
                destreza = int(input("Ingrese destreza (< 20): "))
                if destreza >= 1 and destreza < 20:
                    print("Ingreso exitoso")
                    break
                else:
                    print("Ingresa un valor menor a 20.")
            while True:
                inteligencia = int(input("Ingrese inteligencia (16-20): "))
                if inteligencia >= 16 and inteligencia <= 20:
                    print("Ingreso exitoso")
                    break
                else:
                    print("Ingresa un valor entre 16 y 20.")
            while True:
                carisma = int(input("Ingrese carisma (<20): "))
                if carisma >= 1 and carisma < 20:
                    print("Ingreso exitoso")
                    break
                else:
                    print("Ingresa un valor menor a 20.")
            
        if op == "3":
            print("Creacion de guardabosque:")
            while True:
                fuerza = int(input("Ingrese fuerza (14-18): "))
                if fuerza >= 14 and fuerza <= 18:
                    print("Ingreso exitoso")
                    break
                else:
                    print("Ingresa un valor entre 14 y 18.")
            while True:
                destreza  = int(input("Ingrese destreza (16-20): "))
                if destreza >= 16 and destreza <= 20:
                    print("Ingreso exitoso")
                    break
                else:
                    print("Ingresa un valor entre 16 y 20.")
            while True:
                inteligencia = int(input("Ingrese inteligencia (<20): "))
                if inteligencia >= 1 and inteligencia <20:
                    print("Ingreso exitoso")
                    break
                else:
                    print("Ingresa un valor menor a 20.")
            while True:
                carisma = int(input("Ingrese carisma (< 20): "))
                if carisma >= 1 and carisma < 20:
                    print("Ingreso exitoso")
                    break
                else:
                    print("Ingresa un valor menor a 20.")

    elif op == "2":
        print("<<< Menu configuracion >>>")
    else:
        print("Elija una opcion valida por favor.")
    
