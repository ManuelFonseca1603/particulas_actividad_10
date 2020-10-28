from particula import Particula

class Adm_part:
    def __init__(self):
        self .__particula = []

    def agregar_final(self, particula:Particula):
        self.__particula.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particula.insert(0,particula)

    def mostrar(self):
        for particula in self.__particula:
            print(particula)



l01 = Particula(id=100,origen_x=56,origen_y=34,destino_x=345,destino_y=400,
                velocidad=34,red=23,green=123,blue=200,distancia=0)
#l02 = Particula("200","100","140","400","440","120","300","12","0","0")

# adm_part = Adm_part()
# adm_part.agregar_final(l01)
# adm_part.agregar_inicio(l02)
# adm_part.agregar_inicio(l01)
# adm_part.mostrar()