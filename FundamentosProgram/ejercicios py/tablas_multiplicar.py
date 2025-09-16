#tablas de multiplicar de acuerdo al numero que el usuario ingrese
num = int(input("Ingrese un numero: "))
for i in range(1,11):
    print(num, "x", i, "=", num*i)
    
'''
#que te entrege la tabla anterior a la que ingresaste

num = int(input("Ingrese un numero: "))
for n in range (1, num+1):
    for i in range(1,11):
        print(n, "x", i, "=", n*i)
'''
