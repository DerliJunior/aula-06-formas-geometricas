


from models_formas.FormaGeometrica import FormaGeometrica
from utils.FormaEnum import FormaEnum


class Retangulo(FormaGeometrica):
    def __init__(self, largura: float, altura: float):
        super().__init__(FormaEnum.RETANGULO.value)
        self.__largura = largura
        self.__altura = altura

    def calcular_area(self):
        return self.__largura * self.__altura

    def calcular_perimetro(self):
        return  2 * (self.__largura + self.__altura)

    def getLargura(self):
        return self.__largura

    def setLargura(self, largura):
        self.__largura = largura

    def getAltura(self):
        return self.__altura

    def setAltura(self, altura):
        self.__altura = altura

    def __str__(self):
        return f'Retangulo:{{nome={self.getNome()}, largura={self.getLargura()}, altura={self.getAltura()}, area={self.calcular_area()}, perimetro={self.calcular_perimetro()}}}'


#     - Atributos:
# - largura (private): largura do retângulo.
# - altura (private): altura do retângulo.
# - Métodos:
# - calcular_area(self): implementação do método abstrato.
# - calcular_perimetro(self): implementação do método abstrato.
