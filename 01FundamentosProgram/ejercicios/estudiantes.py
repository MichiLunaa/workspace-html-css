#Un maestro desea saber qué porcentaje de hombres y que porcentaje de mujeres hay en un grupo de estudiantes
# Solicitar el número de hombres y mujeres
num_hombres = int(input("Ingrese el número de hombres en el grupo: "))
num_mujeres = int(input("Ingrese el número de mujeres en el grupo: "))
total_estudiantes = num_hombres + num_mujeres
porcentaje_hombres = (num_hombres / total_estudiantes) * 100
porcentaje_mujeres = (num_mujeres / total_estudiantes) * 100
print("Número total de estudiantes: ", total_estudiantes)
print("Porcentaje de hombres: ", round (porcentaje_hombres, 1) , '%')
print("Porcentaje de mujeres: ", round (porcentaje_mujeres, 1), '%')