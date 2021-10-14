
from os import name


def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()   

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read()
    print(texto)

# ojo o __main__ são dobles under line
if __name__=='__main__':
   #escrever_arquivo('primeira linea.\n')
   #atualizar_arquivo('segunda linea.\n')
   ler_arquivo('teste.txt')
