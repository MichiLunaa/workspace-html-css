#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes: ♦ 55% del promedio de sus tres calificaciones parciales. ♦ 30% de la calificación del examen final. ♦ 15% de la calificación de un trabajo final.
calificacion1 = float(input("Ingrese la calificación del primer parcial: "))
calificacion2 = float(input("Ingrese la calificación del segundo parcial: "))
calificacion3 = float(input("Ingrese la calificación del tercer parcial: "))
examenFinal = float(input("Ingrese la calificación del examen final: "))
trabajoFinal = float(input("Ingrese la calificación del trabajo final: "))
PromedioParciales= (calificacion1 + calificacion2 + calificacion3) / 3
calificacionFinal = (PromedioParciales * 0.55) + (examenFinal * 0.30) + (trabajoFinal * 0.15)
print("La calificación final es: ", calificacionFinal)