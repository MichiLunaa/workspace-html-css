#Diseñe un programa que categorice las notas de la siguiente manera: ♦ Notas entre 1.0 y 2.9 Categoría A ♦ Notas entre 3.0 y 3.9 Categoría B ♦ Notas entre 4.0 y 4.9 Categoría C ♦ Notas entre 5.0 y 5.9 Categoría D ♦ Notas entre 6.0 y 7 Categoría E.
#El usuario ingresa una nota, y se le debe mostrar la categoría a la que pertenece dicha nota. Se debe validar que las notas ingresadas estén dentro de los rangos permitidos: no se aceptan notas menores que 1.0 o mayores que 7. 
nota = float (input('Ingrese su nota (1.0 - 7.0):'))
if nota < 1.0 or nota > 7.0:
    print("Nota inválida. Debe estar entre 1.0 y 7.0.")
elif nota >=6.0:  
    print("Categoría: E")
elif nota >= 5.0:
    print("Categoría: D")
elif nota >= 4.0:
    print("Categoría: C")
elif nota >= 3.0:
    print("Categoría: B")
elif nota >= 1.0:
    print("Categoría: A")