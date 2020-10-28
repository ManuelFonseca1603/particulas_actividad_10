from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self,id=0,origen_x=0,origen_y=0,destino_x=0,destino_y=0,
                velocidad=0,red=0,green=0,blue=0,distancia=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(origen_x, origen_y, destino_x, destino_y)

    def __str__(self):
        return (
            'ID ' + str(self.__id) + '\n' +
            'Origen en x ' + str(self.__origen_x) + '\n' +
            'Origen en y ' + str(self.__origen_y) + '\n' +
            'Destino en x ' + str(self.__destino_x) + '\n' +
            'Destino en y ' + str(self.__destino_y) + '\n' +
            'Velocidad ' + str(self.__velocidad) + '\n' +
            'Red ' + str(self.__red) + '\n' +
            'Green ' + str(self.__green) + '\n' +
            'Blue ' + str(self.__blue) + '\n' +
            'Distancia ' + str(self.__distancia)  
        )

l01 = Particula(id=100,origen_x=56,origen_y=34,destino_x=345,destino_y=400,
                velocidad=34,red=23,green=123,blue=200,distancia=0)
print(l01)
l02 = Particula(id=100,origen_x=156,origen_y=134,destino_x=45,destino_y=409,
                velocidad=34,red=23,green=123,blue=200,distancia=0)
print(l02)