#encontrar los primeros 5 terminos
a=[]
for i in range (5):
    n=i+1
    a.append(3*n+1)
print("Los primeros 5 terminos de la sucesion son: ", a)

#el termino 31 pertene a la sucesion an?
n=0
termino=0
vfinal=31
dif= vfinal - termino
while dif > 0:
    n=n+1
    termino= 3*n + 1
    dif= vfinal - termino
if dif == 0:
    print("El termino 31 pertenece a la sucesion y se encuentra en la posicion: ", n )
else:
    print("El termino 31 no pertenece a la sucesion")