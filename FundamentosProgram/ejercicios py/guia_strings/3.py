#Escriba un programa que construya un string con las letras que coinciden en dos strings ingresados como entrada. Por ejemplo, “amorosos” y “amortiza” coinciden en: “amor”; por otra parte, “conformidad” y “contorno” coinciden en “conor”. Observe que los strings pueden tener distintos largos
palabra1 = input("Ingrese string 1: ")
palabra2 = input("Ingrese string 2: ")
i = 0
while i < len(palabra1):
    print(palabra1[i], palabra2 [i])
    if palabra1[i] == palabra2[i]:
        s = s + palabra1[i]
    i = i + 1
print("String coincidente:, s")
