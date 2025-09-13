#Crear un juego que permita contar la cantidad de vocales que tiene una palabra ingresada por el usuario, en donde sí:
# Tiene 2 vocales o menos informar que perdió
# Si tiene entre 3 y 5 vocales informar que casi gana
# Y si tiene más de 5 informar que ganó
#Pista: Puede usar for para recorrer mediante un ciclo la palabra. Piense cómo puede contar las vocales
palabra=input("Ingrese una palabra: ")
vocales="aeiouAEIOU"
contador=0
for letra in palabra:
    if letra in vocales:
        contador+=1
if contador <=2:
    print("Perdió")
elif contador <=5:
    print("Casi gana")
else:
    print("Ganó")