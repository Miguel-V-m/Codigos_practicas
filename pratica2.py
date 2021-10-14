a = int(input('primeiro bimestre: '))
while a>10:
    a = int(input('você digito errado. o primeiro bimestre: '))
b = int(input('segundo bimestre: '))
while b>10:
    b = int(input('você digito errado. o segundo bimestre: '))
c = int(input('terceiro bimestre: '))
while c>10:
    c = int(input('você digito errado. o terceiro bimestre: '))
d = int(input('quarto bimestre: '))
while d>10:
    d = int(input('você digito errado. o quarto bimestre: '))
media = (a+b+c+d)/4
print('media: {}' .format(media))


# nota = int(input('Eentre com a nota: '))
# while nota>10:
#     nota = int(input('Nota invalida. Entre com a nota correta: '))
# a = 0
# while a<10:
#     print(a)
#     a+=1


#numeron primos que quiser escolher$$$$$$$$
# a = int(input('Entre com um valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div +=1 #div = div + 1
#     if div == 2:
#         print(num) 



##numero primos con sentencia for

# for num in range(101):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div +=1 #div = div + 1
#     if div == 2:
#         print(num)  
    

###calculo de numero primos
# a = int(input('entre com o numero: '))

# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div +=1 #div = div + 1


# if div == 2:
#     print('numero {} é primo: ' .format(a))  
# else:
#     print('numero {} não é primo: ' .format(a))       