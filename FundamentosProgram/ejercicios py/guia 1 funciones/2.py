def IMC(peso, estatura, edad):
    indice = peso / (estatura * estatura)

    if edad < 45 and indice < 22.0:
        return "Bajo"
    elif edad < 45 and indice >= 22.0:
        return "Medio"
    elif edad >= 45 and indice < 22.0:
        return "Medio"
    else:  
        return "Alto"
    
peso = float(input("Ingrese su peso en kilos: "))
estatura = float(input("Ingrese su estatura en metros: "))
edad = int(input("Ingrese su edad: "))

riesgo = IMC(peso, estatura, edad)
print("Su nivel de riesgo es:", riesgo)