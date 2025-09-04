sueldo = int(input("Diga su sueldo: "))
pago = 0
### Sin elif
'''
if sueldo >= 0 and sueldo <= 500000:
    print("Su impuesto es: 0%")
    print("Usted paga:", pago)
if sueldo >= 500001 and sueldo <= 1000000:
    print("Su impuesto es: 2%")
    pago = round(sueldo*(2/100)) # (2/100) el 2 es el % y se divie en 100 para dar 0.02
    print("Usted paga:", pago)
if sueldo >= 1000001 and sueldo <= 2500000:
    print("Su impuesto es: 5%")
    pago = round(sueldo*(5/100))
    print("Usted paga:", pago)
if sueldo >= 2500001: # es igua que: if sueldo > 2500000
    print("Su impuesto es: 12%")
    pago = round(sueldo*(12/100)) # (2/100) el 2 es el % y se divie en 100 para dar 0.02
    print("Usted paga:", pago)
'''

### con elif
if sueldo >= 0 and sueldo <= 500000:
    print("Su impuesto es: 0%")
    print("Usted paga:", pago)
elif sueldo <= 1000000:
    print("Su impuesto es: 2%")
    pago = round(sueldo*(2/100)) # (2/100) el 2 es el % y se divie en 100 para dar 0.02
    print("Usted paga:", pago)
elif sueldo <= 2500000:
    print("Su impuesto es: 5%")
    pago = round(sueldo*(5/100))
    print("Usted paga:", pago)
else: # es igua que: if sueldo > 2500000
    print("Su impuesto es: 12%")
    pago = round(sueldo*(12/100)) # (2/100) el 2 es el % y se divie en 100 para dar 0.02
    print("Usted paga:", pago)

