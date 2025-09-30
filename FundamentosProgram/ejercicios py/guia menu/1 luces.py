#Una empresa de IoT está desarrollando un sistema de control a través de internet de las luces de las viviendas. De esta forma las personas podrán controlar sus luces desde cualquier lugar. Para el desarrollo de este objetivo, usted es contratado tal de que programe una aplicación con dicha funcionalidad. Usted programa un menú con las distintas opciones que se aprecian en la imagen. La particularidad de este sistema es que con la misma opción se puede encender o apagar la luz, si se trata de una luz en particular, puesto que así lo solicitó la empresa. Es decir, usted comienza con todas las luces apagadas, y si elige una opción, la luz se prende y si elige nuevamente la misma opción, ahora la luz debe apagarse.
patio = False
sala = False
pasillo = False
jardin = False

while True:
    print("***** Menú de luces *****") 
    print("1. Encender/apagar Luces patio (Alternado)")
    print("2. Encender/apagar Luces sala (Alternado)")
    print("3. Encender/apagar Luces pasillo (Alternado)")
    print("4. Encender/apagar Luces jardin (Alternado)")
    print("5. Encender todo (Alternado)")
    print("6. Apagar todo (Alternado)")
    print("7. Salir del sistema")
    
    opcion = input("Ingrese la opcion deseada: ")
    if opcion == "1":
        if patio == False:
            print("El patio esta encendido")
            patio = True
        else:
            print("El patio esta apagado")
            patio = False
    elif opcion == "2":
        if sala == False:
            print("La sala esta encendida")
            sala = True
        else:
            print("La sala esta apagada")
            sala = False
    elif opcion == "3":
        if pasillo == False:
            print("El pasillo esta encendido")
            pasillo = True
        else:
            print("El pasillo esta apagado")
            pasillo = False
    elif opcion == "4":
        if jardin == False:
            print("El jardin esta encendido")
            jardin = True
        else:
            print("El jardin esta apagado")
            jardin = False
    elif opcion == "5":
        if patio == False or sala == False or pasillo == False or jardin == False:
            print("Todas las luces encendidas")
            patio = True
            sala = True
            pasillo = True
            jardin = True
        else:
            print("Todas las luces ya estan encendidas")
    elif opcion == "6":
        if patio == True or sala == True or pasillo == True or jardin == True:
            print("Todas las luces apagadas")
            patio = False
            sala = False
            pasillo = False
            jardin = False
        else:
            print("Todas las luces ya estan apagadas")
    elif opcion == "7":        
        print("Hasta pronto...")
        break
    else:
        print("Opción incorrecta, por favor ingrese una opción válida.")



