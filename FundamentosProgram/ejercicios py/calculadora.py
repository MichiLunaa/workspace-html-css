# Calculadora básica con condicionales
num1 = float(input("Operando: "))
operador = input("Operador: ")
num2 = float(input("Operando: "))

if operador == "+":
    print(num1, "+", num2, "=", num1 + num2)

elif operador == "-":
    print(num1, "-", num2, "=", num1 - num2)

elif operador == "*":
    print(num1, "*", num2, "=", num1 * num2)

elif operador == "/":
    print(num1, "/", num2, "=", num1 / num2)

else:
    print("Operador no válido")
