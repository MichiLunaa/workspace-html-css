def mostrar_menu():
    print("\n--- Menú de Sushi ---")
    print("1. Pikachu Roll - $4500")
    print("2. Otaku Roll - $5000")
    print("3. Pulpo Venenoso Roll - $5200")
    print("4. Anguila Eléctrica Roll - $4800")
    print("5. Finalizar pedido")

def aplicar_descuento(total):
    while True:
        tiene_codigo = input("¿Tienes un código de descuento? (s/n): ").lower()
        if tiene_codigo == "s":
            codigo = input("Ingresa el código: ")
            if codigo == "soyotaku":
                print("¡Código válido! Se aplicará un 10% de descuento.")
                return total * 0.9  # Descuento del 10%
            else:
                print("Código no válido.")
                opcion = input("Presiona cualquier tecla para reintentar o 'X' para continuar sin descuento: ").lower()
                if opcion == "x":
                    return total
        elif tiene_codigo == "n":
            return total
        else:
            print("Opción no válida. Intenta nuevamente.")

def mostrar_detalle(pedido, total_final):
    print("\n--- Detalle del Pedido ---")
    total_productos = sum(pedido.values())
    print(f"Total de productos: {total_productos}")
    for roll, cantidad in pedido.items():
        if cantidad > 0:
            print(f"{roll}: {cantidad} unidad(es)")
    print(f"Total a pagar: ${round(total_final)}")

def tomar_pedido():
    precios = {
        "Pikachu Roll": 4500,
        "Otaku Roll": 5000,
        "Pulpo Venenoso Roll": 5200,
        "Anguila Eléctrica Roll": 4800
    }

    pedido = {
        "Pikachu Roll": 0,
        "Otaku Roll": 0,
        "Pulpo Venenoso Roll": 0,
        "Anguila Eléctrica Roll": 0
    }

    total = 0

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            pedido["Pikachu Roll"] += 1
            total += precios["Pikachu Roll"]
            print("Has agregado un Pikachu Roll.")
        elif opcion == "2":
            pedido["Otaku Roll"] += 1
            total += precios["Otaku Roll"]
            print("Has agregado un Otaku Roll.")
        elif opcion == "3":
            pedido["Pulpo Venenoso Roll"] += 1
            total += precios["Pulpo Venenoso Roll"]
            print("Has agregado un Pulpo Venenoso Roll.")
        elif opcion == "4":
            pedido["Anguila Eléctrica Roll"] += 1
            total += precios["Anguila Eléctrica Roll"]
            print("Has agregado un Anguila Eléctrica Roll.")
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

    total_con_descuento = aplicar_descuento(total)
    mostrar_detalle(pedido, total_con_descuento)

# Bucle principal para permitir nuevos pedidos
while True:
    tomar_pedido()
    continuar = input("\n¿Deseas hacer otro pedido? (s/n): ").lower()
    if continuar != "s":
        print("Gracias por tu compra. ¡Hasta la próxima!")
        break
