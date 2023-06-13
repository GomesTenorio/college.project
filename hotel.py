from typing import List
from cliente import Cliente

class Hotel:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.lista_quartos = []

    def add_quarto(self, quarto):
        self.lista_quartos.append(quarto)
        quarto.hotel = self

    def remove_quarto(self, quarto):
        if quarto in self.lista_quartos:
            self.lista_quartos.remove(quarto)

    def consultar_quartos_disponiveis(self):
        quartos_disponiveis = []
        for quarto in self.lista_quartos:
            if not quarto.ocupado:
                quartos_disponiveis.append(quarto)
        return quartos_disponiveis

    def fazer_checkin(self, quarto):
        if quarto in self.lista_quartos and not quarto.ocupado:
            quarto.ocupado = True
            return True
        return False
   
    def listar_clientes(self):
        print("Clientes cadastrados:")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome} - CPF: {cliente.cpf}")