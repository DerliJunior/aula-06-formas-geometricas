from models_formas.Retangulo import Retangulo
from models_formas.Circulo import Circulo
from utils.GerenciarArquivo import GerenciarArquivo


class Main():
    circulo1 = Circulo(5)
    circulo2 = Circulo(7)
    circulo3 = Circulo(10)
    retangulo1 = Retangulo(5, 10)
    retangulo2 = Retangulo(2, 2)
    retangulo3 = Retangulo(8, 15)

    arquivo = GerenciarArquivo('formas.txt')
    arquivo.gravar_arquivo(circulo1)
    arquivo.gravar_arquivo(circulo2)
    arquivo.gravar_arquivo(circulo3)
    arquivo.gravar_arquivo(retangulo1)
    arquivo.gravar_arquivo(retangulo2)
    arquivo.gravar_arquivo(retangulo3)

    print(arquivo.ler_arquivo())

if __name__ == '__main__':
    Main()