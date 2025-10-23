def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero"
    else:
        return a / b

print("Suma:", suma(2, 3))
print("Resta:", resta(7, 2))            
print("Multiplicación:", multiplicacion(4, 3)) 
print("División:", division(10, 2))                 
