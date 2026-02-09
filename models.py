from datetime import datetime


class Produto:
    def __init__(self, codigo, nome, preco, quantidade_estoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque


class Venda:
    def __init__(self, id, produto, quantidade, data):
        self.id = id
        self.produto = produto  # Aqui temos a relação entre objetos: Venda tem um Produto
        self.quantidade = quantidade
        self.data = data