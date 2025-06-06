capitales = {
    'Chile' : 'Santiago',
    'Peru' : 'Lima',
    'Ecuador' : 'Quito'
}
for pais in capitales:
    print(f'La capital de {pais} es {capitales[pais]}')
    
for capital in capitales.values():
    print(capital, 'es una gran ciudad.')
    
for pais, capital in capitales.items():
    print(capital, 'es la capital de', pais)