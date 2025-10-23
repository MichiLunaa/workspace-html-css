def verificar_triangulo(lados):
    a = lados[0]
    b = lados[1]
    c = lados[2]
    
    if a > b + c or b > a + c or c > a + b:
        return "Triángulo inválido"
    else:
        if a == b and b == c:
            return "Triángulo Equilátero"
        elif a == b or a == c or b == c:
            return "Triángulo Isósceles"
        else:
            return "Triángulo Escaleno"

def main():
    lado1 = int(input("Ingrese el primer lado: "))
    lado2 = int(input("Ingrese el segundo lado: "))
    lado3 = int(input("Ingrese el tercer lado: "))
    
    lista_lados = [lado1, lado2, lado3]
    
    resultado = verificar_triangulo(lista_lados)
    print(resultado)

main()
