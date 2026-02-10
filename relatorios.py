from datetime import datetime
import repositorio_produtos
import repositorio_vendas


def produtos_estoque_baixo(limite):
    produtos = repositorio_produtos.carregar_produtos()
    produtos_baixo = []
    
    # Usa o método da classe Produto para verificar estoque baixo
    for produto in produtos:
        if produto.esta_com_estoque_baixo(limite):
            produtos_baixo.append(produto)
    
    return produtos_baixo


def total_vendido_periodo(data_inicio, data_fim):
    vendas = repositorio_vendas.carregar_vendas()
    total = 0
    
    # Usa os métodos das classes Venda para verificar período e calcular total
    for venda in vendas:
        if venda.esta_no_periodo(data_inicio, data_fim):
            total = total + venda.calcular_total()
    
    return total