class Coche():

    def __init__(self):

        self.__largochasis=250
        self.__anchochasi=120
        self.__ruedas=4 #el dos guion bajo impide em modificar una propiedad desde fuera
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            return 'el coche esta en marcha'
        else:
            return 'el coche esta parado'
       

    def estado(self):
        print('El coche tiene', self.__ruedas,'ruedas. Un ancho de', self.__anchochasi,
        'y un largo de', self.__largochasis)
                

miCoche=Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print('------A continuacion creamos el segundo objeto------')

miCoche2=Coche()

print(miCoche2.arrancar(False))

miCoche2.ruedas=2

miCoche2.estado()
