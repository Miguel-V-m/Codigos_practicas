conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
conjunto_união = conjunto.union(conjunto2)
print('união: {} ' .format(conjunto_união))
conjunto_interccão = conjunto.intersection(conjunto2)
print('interseccão: {}' .format(conjunto_interccão))
conjunto_diferencia1 = conjunto.difference(conjunto2)
print('diferencia entre 1 e 2: {}' .format(conjunto_diferencia1))
conjunto_diferencia2 = conjunto2.difference(conjunto)
print('diferencia entre 2 e 1' .format(conjunto_diferencia2))
conjunto_fiff_simetrica = conjunto.symmetric_difference(conjunto2)
print('diferença simetrica: {}' .format(conjunto_fiff_simetrica))

# conjunto = {1,2,3,4}
# conjunto.add(5) #adiciona un elemento en este caso 5
# conjunto.discard(2) # elimina un elemento en este caso 2
# print(conjunto)