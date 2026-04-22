# Loja de jogos
é um sistema simples de cadastro de clientes e jogos, com ambos tendo seus proprios atributos.

## Tecnologia
python 3.13

## Como rodar 
crie objetos como por exemplo
```python
cliente = Cliente('kaique',500)
jogo1 = Jogo_digital('Devil may cry',200,'ps4',50)
cliente.add_jogos(jogo1)
print(jogo1.detalhes())
print(cliente.finalizar_compra())
print(cliente.saldo_atual())
```

## Conceitos de poo aplicados
- Herança — Jogo é a classe base, e JogoFisico e JogoDigital herdam dela com atributos próprios (físico tem estoque, digital tem tamanho em GB)
- Encapsulamento — saldo do cliente é privado, só muda via método de compra
- Polimorfismo — JogoFisico e JogoDigital têm um método detalhes() que se comporta diferente em cada um
- Abstração — a classe base Jogo define o que todo jogo precisa ter, sem implementar tudo
