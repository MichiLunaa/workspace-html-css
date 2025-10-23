
aprobados = 0
reprobados = 0

while True:
    dato = input("Ingrese dato: ")
    
    if dato.lower() == "terminar":
        break
    
    nombre = ""
    nota_str = ""
    encontrado_dos_puntos = False
    
    for letra in dato:
        if letra == ":":
            encontrado_dos_puntos = True
        elif not encontrado_dos_puntos:
            nombre += letra
        else:
            nota_str += letra
    
    nota = float(nota_str)
    
    if nota >= 5.0:
        aprobados += 1
    else:
        reprobados += 1

print("Hubo", aprobados, "estudiantes aprobados y", reprobados, "estudiantes reprobados.")
