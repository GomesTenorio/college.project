from hotel import Hotel

class Quarto:
    def __init__(self, tipo, numero, ocupado, preco):
        self.tipo = tipo
        self.numero = numero
        self.ocupado = False
        self.preco = preco
        self.hotel = None
