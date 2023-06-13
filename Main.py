from hotel import Hotel
from quarto import Quarto
from reserva import Reserva
from cliente import Cliente
from datetime import datetime, timedelta
import random
import pickle

if __name__ == "__main__":

    hotel1 = Hotel("Hotel Maceió", "Av. Ponta Verde")

    quarto1 = Quarto("Quarto solteiro", 101, False, 200)
    hotel1.add_quarto(quarto1)

    quarto2 = Quarto("Suite solteiro", 202, False, 300)
    hotel1.add_quarto(quarto2)

    quarto3 = Quarto("Suite Casal", 303, False, 400)
    hotel1.add_quarto(quarto3)

    quarto4 = Quarto("Suite Presidencial", 404, False, 400)
    hotel1.add_quarto(quarto4)

    clientes = []

    print("DIGITE SUAS INFORMAÇÕES ABAIXO")
    print("------------------------------")
    nome_cliente = input("Nome: ")
    idade_cliente = int(input("Idade: "))
    genero_cliente = input("Gênero: ")
    cpf_cliente = input("CPF: ")
    endereco_cliente = input("Endereço: ")
    telefone_cliente = input("Telefone: ")
    print("------------------------------")

    cliente = Cliente(nome_cliente, idade_cliente, genero_cliente, cpf_cliente, endereco_cliente, telefone_cliente)
    clientes.append(cliente)

#    consultar_clientes = input("Deseja consultar a lista de clientes? (Sim/Não): ")
#    if consultar_clientes.upper() == "Sim":
#        hotel.listar_clientes()
    print("------------------------------")

    quartos_disponiveis = hotel1.consultar_quartos_disponiveis()
    print("Quartos disponíveis:")
    for quarto in quartos_disponiveis:
        print(f"Número: {quarto.numero} - Tipo: {quarto.tipo} - Preço: R${quarto.preco}")

    def atualizar_quartos_disponiveis(quartos_disponiveis, quarto_reservado):
        quartos_disponiveis.remove(quarto_reservado)   

fazer_reservas = True
while fazer_reservas:
    reservar_quarto = input("Deseja fazer uma reserva? (S/N): ")

    if reservar_quarto.upper() == "S":
        if quartos_disponiveis:
            quarto_reservado = None
            while not quarto_reservado:
                numero_quarto = int(input("Digite o número do quarto que deseja reservar: "))

                for quarto in quartos_disponiveis:
                    if quarto.numero == numero_quarto:
                        quarto_reservado = quarto
                        break

                if not quarto_reservado:
                    print("Quarto invalido ou indisponível. Por favor, escolha um quarto disponível.")

            quantidade_dias = int(input("Digite a quantidade de dias da reserva: "))
            codigo_reserva = str(random.randint(100, 999))
            data_inicio = datetime.now()
            data_fim = data_inicio + timedelta(days=quantidade_dias)
            preco_total = quarto_reservado.preco * quantidade_dias
            reserva = Reserva(codigo_reserva, data_inicio, data_fim, preco_total, quarto_reservado)

            if hotel1.fazer_checkin(quarto_reservado):
                print("------------------------------")
                print("Reserva realizada com sucesso!")
                print("------------------------------")
                print()
                print("Dados da reserva:")
                print(f"Hotel: {hotel1.nome}")
                print(f"Endereço: {hotel1.endereco}")
                print(f"Cliente: {nome_cliente}")
                print(f"Código: {codigo_reserva}")
                print(f"Data de início: {reserva.data_inicio}")
                print(f"Data de fim: {reserva.data_fim}")
                print(f"Preço total: R${reserva.preco_final}")
                print(f"Quarto: Número {reserva.quarto.numero} - Tipo: {reserva.quarto.tipo}")
                print()
                print("-------------------------------")
                


                atualizar_quartos_disponiveis(quartos_disponiveis, quarto_reservado)
            else:
                print("Não foi possível fazer a reserva.")
        else:
            print("Não há quartos disponíveis.")
    else:
        print("Reserva não realizada. Obrigado!")

    continuar = input("Deseja continuar com novas reservas? (S/N): ")
    if continuar.upper() != "S":
        fazer_reservas = False

print("Obrigado por utilizar nosso serviço de reservas. Volte sempre!")



