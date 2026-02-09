import csv
from datetime import datetime
from models import Venda, Produto


def carregar_vendas():
    from repositorio_produtos import carregar_produtos
    
    vendas = []
    produtos = carregar_produtos()
    
    try:
        with open('data/vendas.csv', 'r') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # pula o cabeçalho
            for linha in leitor:
                # Encontra o produto correspondente
                codigo_produto = int(linha[1])
                produto = None
                for p in produtos:
                    if p.codigo == codigo_produto:
                        produto = p
                        break
                
                if produto:
                    venda = Venda(int(linha[0]), produto, int(linha[2]), datetime.strptime(linha[3], '%Y-%m-%d %H:%M:%S'))
                    vendas.append(venda)
    except FileNotFoundError:
        pass
    
    return vendas


def salvar_vendas(vendas):
    with open('data/vendas.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'codigo_produto', 'quantidade', 'data'])
        for venda in vendas:
            escritor.writerow([venda.id, venda.produto.codigo, venda.quantidade, venda.data.strftime('%Y-%m-%d %H:%M:%S')])