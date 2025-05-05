#Debe crear un sistema que permita la validación de usuario y contraseña de un empleado en la Empresa XY, los únicos dos usuarios conectados son: a. User_1: karol, Pass_1:1234   b. User_2: shaky,  Pass_2: a4s1
Usuario_1 = input ('Ingrese su nombre de usuario:')
if Usuario_1 != 'karol' :
    print ('Usuario no valido')
contraseñaUser1= int (input('Ingrese su contraseña'))
if contraseñaUser1 != '1234':
    print ('contraseña no valida')
Usuario_2 = input ('Ingrese su nombre de usuario:')
if Usuario_2 != 'shaky' :
    print ('Usuario no valido')
contraseñaUser2= int (input('Ingrese su contraseña'))
if contraseñaUser2 != 'a4s1':
    print ('contraseña invalida') 
    