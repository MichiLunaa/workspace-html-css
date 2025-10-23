cantidad = int(input("¿Cuántos números desea ingresar?: "))

lista_numeros = []
contador = 0

while contador < cantidad:
    numero = int(input("Ingrese un número entero: "))
    lista_numeros.append(numero)
    contador += 1

i = 0
while i < len(lista_numeros):
    j = 0
    while j < len(lista_numeros) - 1:
        if lista_numeros[j] < lista_numeros[j + 1]:
            temp = lista_numeros[j]
            lista_numeros[j] = lista_numeros[j + 1]
            lista_numeros[j + 1] = temp
        j += 1
    i += 1

print("Lista ordenada de mayor a menor:", lista_numeros)
