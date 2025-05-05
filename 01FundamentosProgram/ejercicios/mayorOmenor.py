#dado tres numeros enteros, indique cual de ellos es mayor
Num1= int(input("Indique el primer numero:"))
Num2= int(input("Indique el segundo numero:"))
Num3= int(input("Indique el tercer numero:"))
if Num1>Num2 and Num1>Num3:
    print("El mayor es ", Num1)
elif Num2>Num1 and Num2>Num3:
    print("El mayor es ", Num2)
elif Num3>Num1 and Num3>Num2:
    print("El mayor es ", Num3)
elif Num1==Num2 and Num1==Num3: 
    print("Los tres numeros son iguales")
