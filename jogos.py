from cadastro_clientes import *
from abc import ABC,abstractmethod

class Jogo(ABC):
    def __init__(self,nome,preco,plataforma):
        self.nome = nome
        self.preco = preco
        self.plataforma = plataforma

    @abstractmethod
    def detalhes(self):
        pass



class Jogo_fisico(Jogo):

    def __init__(self, nome, preco, plataforma, estoque=0):
        super().__init__(nome, preco, plataforma)
        self.estoque = estoque

    def detalhes(self):
        return f'jogo:{self.nome} preco:{self.preco} plataforma:{self.plataforma} estoque:{self.estoque}'




    

class Jogo_digital(Jogo):
    def __init__(self,nome,preco,plataforma,tamanho_gb = 0):
        super().__init__(nome,preco,plataforma)
        self.tamanho_gb = tamanho_gb

    def detalhes(self):
        return f'jogo:{self.nome} preco:{self.preco} plataforma:{self.plataforma} tamanho em gb:{self.tamanho_gb}'


