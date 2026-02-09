from datetime import datetime
import repositorio_produtos
import repositorio_vendas


def produtos_estoque_baixo(limite):
    produtos = repositorio_produtos.carregar_produtos()
    produtos_baixo = []
    
    for produto in produtos:
        if produto.quantidade_estoque < limite:
            produtos_baixo.append(produto)
    
    return produtos_baixo


def total_vendido_periodo(data_inicio, data_fim):
    vendas = repositorio_vendas.carregar_vendas()
    total = 0
    
    for venda in vendas:
        if data_inicio <= venda.data <= data_fim:
            total = total + (venda.produto.preco * venda.quantidade)
    
    return total