#Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje que cada uno invierte con respecto a la cantidad total invertida
Cantinversor1 = float(input('Ingrese la cantidad invertida (inversor 1): '))
Cantinversor2 = float(input('Ingrese la cantidad invertida (inversor 2): '))
Cantinversor3 = float(input('Ingrese la cantidad invertida (inversor 3): '))
totalInvertido = Cantinversor1 + Cantinversor2 + Cantinversor3 
porcentaje1 = (Cantinversor1 / totalInvertido) * 100
porcentaje2 = (Cantinversor2 / totalInvertido) * 100
porcentaje3 = (Cantinversor3 / totalInvertido) * 100
print('El porcentaje de inversion del inversor 1 es: ', porcentaje1, '%')
print('El porcentaje de inversion del inversor 2 es: ', porcentaje2, '%')
print('El porcentaje de inversion del inversor 3 es: ', porcentaje3, '%')