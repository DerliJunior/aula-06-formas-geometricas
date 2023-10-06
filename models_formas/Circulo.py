
from models_formas.FormaGeometrica import FormaGeometrica
from utils.FormaEnum import FormaEnum


class Circulo(FormaGeometrica):
    def __init__(self, raio: float):
        super().__init__(FormaEnum.CIRCULO.value)
        self.__raio = raio

    def calcular_area(self):
        return 3.14 * (self.__raio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14 * self.__raio

    def getRaio(self):
        return self.__raio

    def setRaio(self, raio):
        self.__raio = raio

    def __str__(self):
        return f'Circulo:{{nome={self._nome}, raio={self.__raio}, area={self.calcular_area()}, perimetro={self.calcular_perimetro()}}}'