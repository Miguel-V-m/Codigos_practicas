contador = 0
miEmail = input('Introduce tu direccion de email: ')

for i in miEmail:
    if i== '@' or i=='.':
        contador = contador+1


if contador==2:
    print('el email es correcto')  
elif contador>=3:
    print('el email es errado')      
else:
    print('el email es incorrecto')    