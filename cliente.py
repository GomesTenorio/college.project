from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade, genero, cpf, endereco, telefone):
        super().__init__(nome, idade, genero)
        self.__cpf = cpf
        self.__endereco = endereco
        self.__telefone = telefone


    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone