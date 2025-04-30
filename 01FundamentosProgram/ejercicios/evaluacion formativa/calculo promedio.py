#Desarrolle un programa en Python que permita calcular el promedio final de la asignatura deprogramación de algoritmos de un estudiante. El programa debe permitir ingresar la nota dela experiencia de aprendizaje 1, 2 y 3. Donde cada nota tiene una ponderación de 30%, 40% y 30%. Este promedio (promedio de presentación de examen) debe mostrarse por pantalla.Luego, el programa debe permitir ingresar la nota del Examen transversal y calcular el promedio final. Recuerde que el promedio final se calcula como 60% el promedio de presentación y 40% la nota del examen
Nota1 = float(input("Ingrese la nota de la EA1: "))
Nota2 = float(input("Ingrese la nota de la EA2: "))
Nota3 = float(input("Ingrese la nota de la EA3: "))
ponderacion1= Nota1 * 0.3
ponderacion2= Nota2 * 0.4
ponderacion3= Nota3 * 0.3
promedioPresentacion= (ponderacion1 + ponderacion2 + ponderacion3) 
print ('Tu promedio de presentacion a examen es: ', promedioPresentacion)
notaExamen = float (input('Ingrese la nota de su examen: '))
promedioFinal = (promedioPresentacion * 0.6) + (notaExamen * 0.4)
print ('Tu promedio final es: ' , promedioFinal)