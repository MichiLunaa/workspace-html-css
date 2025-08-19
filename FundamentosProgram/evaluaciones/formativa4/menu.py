turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"]
}
def turistas_por_pais(pais):
    encontrados = []
    for datos in turistas.values():
        if datos[1].lower() == pais.lower():
            encontrados.append(datos[0])
    if encontrados:
        print(f"Turistas de {pais}:")
        for nombre in encontrados:
            print(f"- {nombre}")
    else:
        print(f"No se encontraron turistas del país: {pais}")

def turistas_por_mes(mes):
    total = len(turistas)
    cantidad = 0
    for datos in turistas.values():
        fecha = datos[2]
        mes_turista = int(fecha.split("-")[1])
        if mes_turista == mes:
            cantidad += 1
    porcentaje = (cantidad / total) * 100
    return round(porcentaje, 1)

def eliminar_turista():
    nombre_ingresado = input("Ingrese el nombre del turista a eliminar: ").lower()
    eliminado = False

    for clave, datos in list(turistas.items()):
        if datos[0].lower() == nombre_ingresado:
            del turistas[clave]
            eliminado = True
            print("Turista eliminado con éxito.")
            break
    if not eliminado:
        print("Turista no encontrado. No se pudo eliminar.")

def main():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1.- Turistas por país")
        print("2.- Turista por mes")
        print("3.- Eliminar turista")
        print("4.- Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pais = input("Ingrese el país: ")
            turistas_por_pais(pais)

        elif opcion == "2":
            while True:
                try:
                    mes = int(input("Ingrese el número del mes (1 al 12): "))
                    if 1 <= mes <= 12:
                        porcentaje = turistas_por_mes(mes)
                        print(f"Porcentaje de turistas que ingresaron en el mes {mes}: {porcentaje}%")
                        break
                    else:
                        print("Mes inválido. Debe estar entre 1 y 12.")
                except ValueError:
                    print("Debe ingresar un número válido.")

        elif opcion == "3":
            eliminar_turista()

        elif opcion == "4":
            print("Programa terminado...")
            break

        else:
            print("Debe seleccionar una opción válida.")

main()
