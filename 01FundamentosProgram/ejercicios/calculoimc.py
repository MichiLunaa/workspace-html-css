# formula: peso (kg) / altura (m) ^ 2
peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu altura en metros: "))
imc = peso / (estatura ** 2)
imc = round(imc, 1)
print(f"Tu indice de masa corporal es: {imc} ") 
if imc < 18.5:
    print("bajo peso")
elif imc <= 24.9:
    print("peso normal")
elif imc <= 29.9:
    print("sobrepeso")
elif imc <= 34.9:
    print("obesidad grado 1")
elif imc <= 39.9: 
    print("obesidad grado 2")
else: 
    print("obesidad grado 3") 