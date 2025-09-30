#En el restaurant Sushipy, el jefe de local quiere conocer estadísticas de los almuerzos más vendidos. Los almuerzos consisten en un plato de fondo y postre opcional. Para ello le solicitan a usted que haga un programa en el que se solicite el precio del plato vendido (si ingresa -1 termina el proceso). Hay clientes muy golosos, que piden 1 o más postres. Por lo que se debe ingresar el monto del o de los postres, hasta que se ingrese un 0. Entregue el precio del plato de fondo más caro y a que cliente pertenece, la cantidad de postres solicitados en total, el valor promedio de todos los almuerzos, y la cantidad de clientes atendidos. 
precio_plato = 0
precio_postre = 0
plato_mas_caro = 0
cliente_plato_caro = 0
cantidad_postres = 0
suma_total = 0
cantidad_clientes = 0   
cliente = 1
precio_plato = int(input("Ingrese monto plato: "))
while precio_plato != -1: 
    cantidad_clientes = cantidad_clientes + 1
    suma_total_almuerzos = suma_total + precio_plato
    precio_postre = int(input("Ingrese monto postre: "))
    while precio_postre != 0:
        cantidad_postres = cantidad_postres + 1
        suma_total_almuerzos = suma_total_almuerzos + precio_postre
        precio_postre = int(input("Ingrese monto postre: "))
        if precio_plato > plato_mas_caro:
         plato_mas_caro = precio_plato
         cliente_plato_caro = cliente
         suma_total = suma_total_almuerzos
        suma_total= suma_total_almuerzos
        cliente= cliente + 1
        suma_total= suma_total_almuerzos
    cliente = cliente +1
    precio_plato = int(input("Ingrese monto plato: "))
if cantidad_clientes != 0:
    promedio_almuerzos = suma_total / cantidad_clientes
else:
    promedio_almuerzos = 0
    
    
print("**** Estadisticas ****")
if plato_mas_caro != 0:
    print("El plato mas caro costo:", plato_mas_caro, "y pertenece al cliente:", cliente_plato_caro)
else:
    print("El plato mas caro costo: 0 y no pertenece a ningun cliente:")
print("La cantidad de postres solicitados fue de:", cantidad_postres)
print("El valor promedio de las ventas es de:", promedio_almuerzos)
print("Cantidad de clientes:", cantidad_clientes)   
    