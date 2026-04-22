from cadastro_clientes import Cliente
from jogos import *
from jogos import Jogo

cliente = Cliente('kaique',500)
jogo1 = Jogo_digital('Devil may cry',200,'ps4',50)
cliente.add_jogos(jogo1)
print(jogo1.detalhes())
print(cliente.finalizar_compra())
print(cliente.saldo_atual())

