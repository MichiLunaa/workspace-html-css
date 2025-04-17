#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra
total_compra = float(input('Ingrese el total de la compra: $'))
descuentoporcentaje = 0.15
descuento = total_compra * 0.15
total_final = total_compra - descuento
print('El total de la compra es: $', total_compra)
print('El descuento es: $', descuento)
print('El total a pagar es: $', total_final)