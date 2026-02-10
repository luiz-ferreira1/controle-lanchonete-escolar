from datetime import datetime


class Produto:
    def __init__(self, codigo, nome, preco, quantidade_estoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
    
    def tem_estoque_suficiente(self, quantidade):
        """Verifica se há estoque suficiente para a quantidade solicitada"""
        return self.quantidade_estoque >= quantidade
    
    def diminuir_estoque(self, quantidade):
        """Diminui o estoque do produto pela quantidade vendida"""
        self.quantidade_estoque = self.quantidade_estoque - quantidade
    
    def esta_com_estoque_baixo(self, limite):
        """Verifica se o produto está com estoque abaixo do limite"""
        return self.quantidade_estoque < limite
    
    def validar_preco(self):
        """Valida se o preço é positivo"""
        return self.preco > 0
    
    def validar_estoque(self):
        """Valida se a quantidade em estoque é positiva"""
        return self.quantidade_estoque > 0


class Venda:
    def __init__(self, id, produto, quantidade, data):
        self.id = id
        self.produto = produto  # Aqui temos a relação entre objetos: Venda tem um Produto
        self.quantidade = quantidade
        self.data = data
    
    def calcular_total(self):
        """Calcula o valor total da venda"""
        return self.produto.preco * self.quantidade
    
    def esta_no_periodo(self, data_inicio, data_fim):
        """Verifica se a venda está dentro do período especificado"""
        return data_inicio <= self.data <= data_fim