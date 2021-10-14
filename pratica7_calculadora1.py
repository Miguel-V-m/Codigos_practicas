class Calculadora:
    def __init__(self,num1, num2):
        self.a=num1
        self.b=num2
    def soma(self): #define 
        return self.a + self.b # retorna
    def subtação(self):
        return self.a - self.b
    def multiplicação(self):
        return self.a*self.b
    def divição(self):
        return self.a/self.b   
if __name__== '_maim_':        
    calculadora =  Calculadora(10,2)
    print(calculadora.a)
    print(calculadora.soma())
    print(calculadora.subtação())
    print(calculadora.multiplicação())
    print(calculadora.divição())