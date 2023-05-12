from Computador import Computador

class Notebook(Computador):

    def __init__(self, modelo=None, cor=None, preco = None, tempoDeBateria = None):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def cadastrar(self):
        super().getInformacoes()
        print("Tempo de bateria: ", self.__tempoDeBateria)
