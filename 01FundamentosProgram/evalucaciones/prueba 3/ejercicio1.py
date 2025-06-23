def pedir_numero_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

def main():
    # Pedir cuántos pacientes se registrarán
    N = pedir_numero_entero("Ingrese la cantidad de pacientes a registrar: ")

    mas_de_dos = 0
    dos_o_menos = 0

    for i in range(1, N + 1):
        print(f"\nPaciente {i}:")
        tratamientos = pedir_numero_entero("Ingrese la cantidad de tratamientos realizados: ")

        if tratamientos > 2:
            print("Más de 2 tratamientos.")
            mas_de_dos += 1
        else:
            print("2 o menos tratamientos.")
            dos_o_menos += 1

    # Resultados finales
    print("\n--- RESULTADOS ---")
    print(f"Pacientes con más de 2 tratamientos: {mas_de_dos}")
    print(f"Pacientes con 2 o menos tratamientos: {dos_o_menos}")

# Ejecutar el programa
main()
