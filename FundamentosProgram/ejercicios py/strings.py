nombre = input ("Ingrese nombre: ")
inicial = nombre [0]
print ("El nombre comienza con: ", inicial)
print ("El nombre termina con: ", nombre [-1])
print ("El nombre tiene ", len(nombre), " letras") #cantidad de cracteres
if len(nombre) %2 == 1:
    indice =  round ((len(nombre)/2) - 0.5)
    letra_almedio = nombre [indice]
    print ("La letra al medio es: ", letra_almedio)
else:
    indice2 = len(nombre)//2
    indice1 = (len(nombre)//2) - 1 
    letra_almedio = nombre [indice1] + nombre [indice2]
    print ("Las letras al medio son: ", letra_almedio)

