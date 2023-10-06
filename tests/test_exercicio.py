

from models_formas.Circulo import Circulo


def test_calcula_area():
    circulo1 = Circulo(6).getRaio() > 0
    assert circulo1 == True
    
def test_calcula_perimetro():
    circulo2 = Circulo(10).getRaio() > 0
    assert circulo2 == False

def test_calcular_area_retangulo_igual_314():
    circulo3 = Circulo(10).calcular_area() == 314.0
    assert circulo3 == True