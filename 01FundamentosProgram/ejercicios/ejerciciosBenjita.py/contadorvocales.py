#Pide al usuario una palabra y muestra cuántas vocales contiene.
palabra = input("Introduce una palabra: ")
vocales = 0
for letra in palabra:
    if letra in "aeiouAEIOU":
        vocales += 1
print(f"La palabra contiene {vocales} vocales.")