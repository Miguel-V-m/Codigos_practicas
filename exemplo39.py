# codificamos una lista en codigo binario y rescatarlo
import pickle

# lista_nombres=['Oedro','Ana','Maria','Isabel']

# fichero_binario = open('lista_nombres','wb')
# pickle.dump(lista_nombres,fichero_binario)
# fichero_binario.close()
# del (fichero_binario)
fichero=open('lista_nombres','rb')
lista=pickle.load(fichero)

print(lista)