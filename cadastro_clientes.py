import jogos
from jogos import *
from abc import ABC,abstractmethod
class Cliente:
    def __init__(self,nome,saldo):
        self.nome = nome
        self.__saldo = saldo
        self.carrinho = []
        self.historico = []



    def add_jogos(self,jogo):
        self.carrinho.append(jogo)

    def saldo_atual(self):
        return  self.__saldo

    def finalizar_compra(self):
        total_compra = sum(jogo.preco for jogo in self.carrinho)
        if self.__saldo >= total_compra:
            self.__saldo -= total_compra
            self.historico.append(self.carrinho.copy())
            self.carrinho.clear()
            return f'Compra finalizada! saldo restante: {self.__saldo}'
        else:
            return f'Saldo insuficiente! total da compra: {total_compra}| Saldo atual {self.__saldo} '











