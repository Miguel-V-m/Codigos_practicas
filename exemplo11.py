lista = [1,10]
arquivo = open('teste.txt','r')
try:
    texto = arquivo.read()
    divisao = 10/1
    numero = lista[1]
except ZeroDivisionError:
    print('não é posivel realizar uma divisao por 0')    
except IndexError:
    print('erro ao acessar um indice invalido da lista')   
except BaseException as ex:
    print('Erro desconhecido: {}' .format(ex))  
else:
    print('Executar quando não ocorre exceção')   
finally:
    print('sempre executa')   
    print('fechando arquivo')
    arquivo.close()    