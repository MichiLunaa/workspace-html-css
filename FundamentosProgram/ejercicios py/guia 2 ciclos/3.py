precio_paracetamol = 2490
precio_tapsin = 4990
precio_vitaminaC = 990
precio_nastizol = 6690

cant_paracetamol = 0
cant_tapsin = 0
cant_vitaminaC = 0
cant_nastizol = 0

opcion = 0
while opcion != 5:
    print("1) Paracetamol")
    print("2) Tapsin")
    print("3) Vitamina C")
    print("4) Nastizol")
    print("5) Salir")
    opcion = int(input("Seleccione medicamento: "))

    if opcion == 1:
        unidades = int(input("Ingrese cuantas unidades desea: "))
        cant_paracetamol = cant_paracetamol + unidades
    else:
        if opcion == 2:
            unidades = int(input("Ingrese cuantas unidades desea: "))
            cant_tapsin = cant_tapsin + unidades
        else:
            if opcion == 3:
                unidades = int(input("Ingrese cuantas unidades desea: "))
                cant_vitaminaC = cant_vitaminaC + unidades
            else:
                if opcion == 4:
                    unidades = int(input("Ingrese cuantas unidades desea: "))
                    cant_nastizol = cant_nastizol + unidades
                else:
                    if opcion != 5:
                        print("Opción inválida")

total = (cant_paracetamol * precio_paracetamol) + (cant_tapsin * precio_tapsin) + (cant_vitaminaC * precio_vitaminaC) + (cant_nastizol * precio_nastizol)

print("El total de medicamentos vendidos es:")
print("---------------------------------------")
print("Paracetamol:", cant_paracetamol)
print("Tapsin:", cant_tapsin)
print("Vitamina C:", cant_vitaminaC)
print("Nastizol:", cant_nastizol)
print("---------------------------------------")
print("El total de ventas es $", total)

if total > 500000:
    print("Éxito de ventas")
else:
    print("Se deben realizar ofertas")
