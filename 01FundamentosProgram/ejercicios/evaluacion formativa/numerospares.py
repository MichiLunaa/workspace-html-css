#Desarrolle un programa que reciba 3 números por teclado, uno por uno, y diga: cuántos números son pares y cuantos impares. Además, debe indicar si la suma de todos los números es mayor a 100. Si lo es, debe indicar si la suma es par o impar
Num1 = int(input("Ingrese el primer número: "))
Num2 = int(input("Ingrese el segundo número: "))
Num3 = int(input("Ingrese el tercer número: "))
suma = Num1 + Num2 + Num3
pares = 0
impares = 0
if Num1 % 2 == 0:
    pares += 1
else:
    impares += 1

if Num2 % 2 == 0:
    pares += 1
else:
    impares += 1
    
if Num3 % 2 == 0:
    pares += 1
else:
    impares += 1
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
if suma > 100:
    print("La suma de los números es mayor a 100")
else:
    print("La suma de los números no es mayor a 100")
if suma % 2 == 0:
    print("La suma es par")
else:
    print("La suma es impar")
