import csv
from models import Produto


def carregar_produtos():
    produtos = []
    try:
        with open('data/produtos.csv', 'r') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # pula o cabeçalho
            for linha in leitor:
                produto = Produto(int(linha[0]), linha[1], float(linha[2]), int(linha[3]))
                produtos.append(produto)
    except FileNotFoundError:
        pass
    return produtos


def salvar_produtos(produtos):
    with open('data/produtos.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['codigo', 'nome', 'preco', 'quantidade_estoque'])
        for produto in produtos:
            escritor.writerow([produto.codigo, produto.nome, produto.preco, produto.quantidade_estoque])