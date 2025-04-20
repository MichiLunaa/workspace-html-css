# Escribe un programa que imprima todos los números pares entre 1 y 100.

initialNum = 1
finalNum = 101

# Utilizando FOR
for initialNum in range(1, finalNum):
    if initialNum % 2 == 0:
        print(initialNum)

# Utilizando WHILE
# while initialNum <= 100:
#     if initialNum % 2 == 0:
#         print(initialNum)
#     initialNum += 1
