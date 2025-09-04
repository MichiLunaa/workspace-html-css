dist = float(input("Distancia: "))
angulo = float(input("Angulo: "))

if dist <= 7:
    print("Pileta")
elif dist > 47:
    print("Fuera de la plaza")
elif angulo >= 45 and angulo <= 90:
    if dist > 7 and dist <= 47:
        print("Publico")
elif dist >= 20 and dist <= 35:
    if (angulo >= 0 and angulo <= 45) or (angulo >= 90 and angulo <= 135): # area 1 y 2
        print("Area Verde")
    elif angulo >= 180 and angulo <= 225: # area 3
        print("Area verde")
    elif angulo >= 270 and angulo <= 315: # area 4
        print("Area verde")
    else:
        print("Cemento")
else:
    print("Cemento")

    