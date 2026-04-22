from jogos import *
from abc import ABC,abstractmethod
class Cliente:
    def __init__(self,nome,saldo):
        self.nome = nome
        self.__saldo = saldo


    def add_jogos(self,carrinho):
        pass
