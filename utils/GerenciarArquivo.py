class GerenciarArquivo:
    def __init__(self, nome_arquivo: str):
        self.nome_arquivo = nome_arquivo

    def gravar_arquivo(self, forma: str):
        with open(self.nome_arquivo, 'a') as arquivo:
                arquivo.write(f'{forma}\n')

    def ler_arquivo(self):
        formas: str = ''
        with open(self.nome_arquivo, 'r') as arquivo:
            for linha in arquivo.readlines():
                    formas += linha
        return formas