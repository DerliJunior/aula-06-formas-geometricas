from abc import abstractmethod

class FormaGeometrica:
    def __init__(self, nome: str):
        self._nome = nome


#  - calcular_area(self): método abstrato que retorna a área da forma.
    @abstractmethod
    def calcular_area(self):
        pass

# - calcular_perimetro(self): método abstrato que retorna o perímetro da forma.
    @abstractmethod
    def calcular_perimetro(self):
        pass

    def getNome(self):
        return self._nome
    
    def setNome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'FormaGeometrica(nome={self._nome})'
