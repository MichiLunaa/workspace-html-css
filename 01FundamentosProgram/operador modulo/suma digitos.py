#para sumar digitos de un numero
n = int(input("Ingrese número: "))
n1= n%10
print ("el ultimo digito es:", n1)
n2= (n//10)
print ("la cifra nueva es: ", n2)
n3= n2%10
print ("el digito del medio es:", n3)
n4= (n2//10)
print ("El ultimo digito es: ", n4)
print ("*****************")
print ("La suma de los digitos es: ", n1+n3+n4)
