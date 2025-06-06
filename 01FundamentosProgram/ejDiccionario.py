d1 = {
    'nombre': 'Pato lucas',
    'edad': 12,
    'rut' : '123-4'
}
print(d1)
#accediendi por la key
print(d1['nombre'])
d1['nombre'] = 'Pata Daisy'
print(d1)
d1['direccion'] = 'Sucasa #123'
print(d1)
print('/#backslash nImprimir VALUE')
for clave, valor in d1.items:
    print(clave , valor)