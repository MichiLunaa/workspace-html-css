cantestudiantes = int(input("Cantidad de estudiantes: "))

sin_bono = 0
bono_05 = 0
bono_08 = 0
bono_10 = 0

suma_notas = 0
nota_mayor = 0

i = 1
while i <= cantestudiantes: 
    nota = float(input("Ingrese nota: "))
    suma_notas = suma_notas + nota

    if nota > nota_mayor:
        nota_mayor = nota

    if nota < 4.0:
        bono = 0.0
        sin_bono = sin_bono + 1
    else:
        if nota >= 4.0 and nota <= 5.0:
            bono = 0.5
            bono_05 = bono_05 + 1
        else:
            if nota >= 5.1 and nota <= 6.0:
                bono = 0.8
                bono_08 = bono_08 + 1
            else:
                if nota >= 6.1 and nota <= 7.0:
                    bono = 1.0
                    bono_10 = bono_10 + 1
                else:
                    bono = 0.0
                    sin_bono = sin_bono + 1
    
    print("El bono para este estudiante es:", bono)
    i = i + 1

promedio = suma_notas / cantestudiantes

print("***** Estadística *****")
print("Cantidad de alumnos sin bono:", sin_bono)
print("Cantidad de alumnos con bono 0.5:", bono_05)
print("Cantidad de alumnos con bono 0.8:", bono_08)
print("Cantidad de alumnos con bono 1.0:", bono_10)
print("La nota mayor es:", (nota_mayor))
print("Promedio de notas:", (promedio))
