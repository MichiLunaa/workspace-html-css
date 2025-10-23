def calculo(sueldo, num_hijos):
    if sueldo <= 250000 and num_hijos <= 1:
        return "Póliza A"
    elif sueldo > 250000 and num_hijos == 0:
        return "Póliza B"
    elif sueldo > 250000 and num_hijos >= 1 and num_hijos <= 5:
        return "Póliza C"
    else:
        return "Póliza D"

def main():
    sueldo = int(input("Ingrese su sueldo: "))
    num_hijos = int(input("Ingrese el número de hijos: "))
    
    poliza = calculo(sueldo, num_hijos)
    
    print("Le corresponde la", poliza)

main()
