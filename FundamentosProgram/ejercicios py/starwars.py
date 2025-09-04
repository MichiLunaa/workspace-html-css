#constantes por unidad
nevarro_grasa = 1.9
nevarro_carbo = 6
nevarro_prote = 0.8

soup_grasa = 10
soup_carbo = 12
soup_prote = 11

# inputs
nevarro = float(input("Nevarro Nummies consumidas (en unidades): "))
soup = int(input("Space Soup consumida (en [ml]): "))
rana = int(input("Carne de rana consumida (en [g]): "))

# calculos
grasa_nevarro = nevarro * nevarro_grasa # la cantidad de nevarro por lo que aporta cada unida de nevarro
carbo_nevarro = nevarro * nevarro_carbo
prote_nevarro = nevarro * nevarro_prote

grasa_soup_1ml = soup_grasa/285 # me permite calcular el aporte por ml
carbo_soup_1ml = soup_carbo/285
prote_soup_1ml = soup_prote/285

grasa_soup = soup * grasa_soup_1ml # la cantidad de sopa por lo que aporta cada unida de nevarro
carbo_soup = soup * carbo_soup_1ml
prote_soup = soup * prote_soup_1ml

### hacemos mas corto el calculo para la carne
grasa_rana_1gr = 0.003 # 0.3/100
carbo_rana_1gr = 0
prote_rana_1gr = 0.16 # 16/100

grasa_rana = rana * grasa_rana_1gr
carbo_rana = 0
prote_rana = rana * prote_rana_1gr

total_grasa = round(grasa_nevarro + grasa_soup + grasa_rana,2)
total_carbo = round(carbo_nevarro + carbo_soup + carbo_rana,2)
total_prote = round(prote_nevarro + prote_soup + prote_rana,2)

#prints
print("Grogu ha consumido: ")
print(total_grasa, "[g] de grasas")
print(total_carbo, "[g] de carbohidratos")
print(total_prote, "[g] de proteinas")