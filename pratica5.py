Lista = [12,10,5,7]
Lista_animal = ['cachorro', 'gato', 'elefante','lobo','arara']
#TUPLAS
Lista_animal[0] = 'macaco'
print(Lista_animal)

tupla = (1,10,12,14)
print(len(tupla)) # o "len" da o numero de elementos de uan lista
print(len(Lista_animal))
tupla_animal = tuple(Lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numererica = list(tupla)
print(type(lista_numererica))
print(lista_numererica)

# Lista.sort() #ordena de menor a maior
# Lista_animal.sort()
# print(Lista)
# print(Lista_animal)
# Lista_animal.reverse() #ordena de forma invertida
# print(Lista_animal)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$
# Lista = [1,3,5,7]
# Lista_animal = ['cachorro', 'gato', 'elefante']
# #print(Lista_animal[1]) # como o conteo no ppython comensa de cero "gato seria 1 "
# print(sum(Lista)) # da a soma total da lista
# print(max(Lista)) #da o maior valor da lista
# print(min(Lista)) #da o menor valor da lista
# print(max(Lista_animal)) #da o maior valor da lista (ordem alfabetico)
# print(min(Lista_animal)) #da o menor valor da lista (ordem alfabetico)
# #nova_lista = Lista_animal*3 # multiplica por 3 cada elemento da lista
# #print(nova_lista)
# if 'lobo' in Lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe u lobo na lista. Sera incluido')    
#     Lista_animal.append('lobo') #agrega un elemento como o caso "lobo"
#     print(Lista_animal)

# #Lista_animal.pop() #o "pop(aqui é a orden de exlusão)" retira o ultimo elemento que agrego na lista  como o caso "lobo"
# Lista_animal.remove('elefante')
# print(Lista_animal)

#########################################################################
############################################################3
#todo o mentado abaixo pode resumir o que esta acima (print(sum(Lista)))
# soma=0
# for x in Lista:
#     print(x)
#     soma += x
# print(soma)