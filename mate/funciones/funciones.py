#definicion de una funcion y calculo de una imagen
def s(x):
    s= 40-10*x
    return s
print(s(3))  

x= 0
while 40 - 10*x > 0:
    x = x + 1
    print(f'la pelota alcanza su altura maxima a los {x} segundos')