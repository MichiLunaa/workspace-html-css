def mostrar_menu():
    print("\n*** MENU PRINCIPAL ***")
    print("1.- Ingresar número.")
    print("2.- Mostrar mayor.")
    print("3.- Mostrar total de números ingresados.")
    print("4.- Salir.")

def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero entre 0 y 100: "))
            if 0 <= numero <= 100:
                print("Ingreso exitoso")
                return numero
            else:
                print("Debe ingresar un número entre 0 y 100!!")
        except ValueError:
            print("Debe ingresar un número entero!!")

def main():
    numeros = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = pedir_numero()
            numeros.append(numero)

        elif opcion == "2":
            if len(numeros) == 0:
                print("No se han ingresado números.")
            else:
                print("El número mayor ingresado es:", max(numeros))

        elif opcion == "3":
            if len(numeros) == 0:
                print("No se han ingresado números.")
            else:
                print("Total de números ingresados:", len(numeros))

        elif opcion == "4":
            print("Fin del programa. Adiós.")
            break

        else:
            print("Debe ingresar una opción válida.")

# Ejecutar el programa
main()
