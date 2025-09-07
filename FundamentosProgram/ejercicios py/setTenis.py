# Programa: Determinar el resultado de un set de tenis

a = int(input("Juegos ganados por A: "))
b = int(input("Juegos ganados por B: "))

if a == 6 and b <= 4:
    print("Gano A")
elif b == 6 and a <= 4:
    print("Gano B")
elif a == 7 and (b == 5 or b == 6):
    print("Gano A")
elif b == 7 and (a == 5 or a == 6):
    print("Gano B")
elif (a < 6 and b < 6) or (a == 6 and b == 5) or (b == 6 and a == 5):
    print("Aun no termina")
else:
    print("Invalido")
