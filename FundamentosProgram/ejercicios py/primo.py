n = int (input("Ingrese un numero entero: "))
c = 2
primo = True
while c < n:
    if n % c == 0:
        print("El numero no es primo")
        primo = False
        break
    c = c + 1
if primo == True:
    print("El numero es primo")