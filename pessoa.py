class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.__idade = idade
        self.__genero = genero

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        return self.__genero