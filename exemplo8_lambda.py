from aula8_contador_letras import contador_letras


contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro','gato','elefante']
print(contador_letras(lista_animais))
#lo mismo para las cuatro operaciones
soma = lambda a, b: a+b

print(soma(5,10))

#crear una calculadora usando lambda
calculadora = {
    'soma': lambda a, b: a+b,
    'subtacao': lambda a, b: a-b,
    'multiplicacao': lambda a, b: a*b,
    'divicao': lambda a, b: a/b,
}

print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
print('a soma é: {}' .format(soma(10,5)))
print('A multiplicacao é: {}' .format(multiplicacao(10,2)))