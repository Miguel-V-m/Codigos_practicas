class Calculadora:
    # def __init__(self):
    #     pass
    def soma(self,a,b): #define 
        return a + b # retorna
    def subtação(self,a,b):
        return a - b
    def multiplicação(self,a,b):
        return a*b
    def divição(self,a,b):
        return a/b   
calculadora =  Calculadora()
print(calculadora.soma(5,2))
print(calculadora.subtação(8,6))
print(calculadora.multiplicação(9,5))
print(calculadora.divição(7,5))