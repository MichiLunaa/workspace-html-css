mayor = float("-inf") # menos infinito
for i in range (5):
    n=int(input("Ingrese un numero: "))
    if n > mayor:
        mayor = n
print ("el numero mayor es: ", mayor)