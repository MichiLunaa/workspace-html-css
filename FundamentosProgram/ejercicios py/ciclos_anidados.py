# dados

# con while
'''
i = 1
while i <= 6:
    j = 1
    while j <= 6:
        print(i,j)
        j = j + 1
    i = i + 1
'''

# ahora con for
for i in range(1,7): #para que incluya al 6, se pone 7
    for j in range(1,7):
        print(i,j)