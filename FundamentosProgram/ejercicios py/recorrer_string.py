password = input("Ingrese su contraseña: ")
contador = 0
for c in password:
    if c in "0123456789":
        contador = contador + 1
        
print("La contraseña tiene", contador, "números")