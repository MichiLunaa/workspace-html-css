# Calcular el sueldo bruto de un trabajador en función del número de horas trabajadas y del valor de la hora de trabajo. Además, calcular el sueldo líquido, considerando los descuentos fijos por conceptos de impuestos (21%)

valorhora = int(input("Ingrese el valor de la hora trabajda:$"))
horastrabajadas = float(input("Ingrese horas trabajadas:"))

sbruto = valorhora * horastrabajadas
sliquido = round(sbruto, 1) - (sbruto * 0.21)

print("Su sueldo bruto es: $", sbruto)
print("Su sueldo liquido es: $", sliquido)
