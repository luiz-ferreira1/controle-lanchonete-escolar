from datetime import datetime
from models import Produto, Venda
import repositorio_produtos
import repositorio_vendas
import relatorios


def menu_principal():
    print("\n=== LANCHONETE ESCOLAR ===")
    print("1 - Produtos")
    print("2 - Vendas")
    print("3 - Relatórios")
    print("0 - Sair")
    opcao = input("Escolha: ")
    return opcao


def menu_produtos():
    print("\n=== MENU PRODUTOS ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("0 - Voltar")
    opcao = input("Escolha: ")
    return opcao


def menu_vendas():
    print("\n=== MENU VENDAS ===")
    print("1 - Registrar venda")
    print("0 - Voltar")
    opcao = input("Escolha: ")
    return opcao


def menu_relatorios():
    print("\n=== MENU RELATÓRIOS ===")
    print("1 - Produtos com estoque baixo")
    print("2 - Total vendido no dia")
    print("0 - Voltar")
    opcao = input("Escolha: ")
    return opcao


def cadastrar_produto():
    produtos = repositorio_produtos.carregar_produtos()
    
    # gera novo codigo
    if len(produtos) > 0:
        maior_codigo = 0
        for p in produtos:
            if p.codigo > maior_codigo:
                maior_codigo = p.codigo
        novo_codigo = maior_codigo + 1
    else:
        novo_codigo = 1
    
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade em estoque: "))
    
    produto = Produto(novo_codigo, nome, preco, quantidade)
    produtos.append(produto)
    
    repositorio_produtos.salvar_produtos(produtos)
    print("Produto cadastrado!")


def listar_produtos():
    produtos = repositorio_produtos.carregar_produtos()
    
    print("\n=== LISTA DE PRODUTOS ===")
    for produto in produtos:
        print(f"{produto.codigo} - {produto.nome} - R$ {produto.preco} - Estoque: {produto.quantidade_estoque}")


def registrar_venda():
    produtos = repositorio_produtos.carregar_produtos()
    vendas = repositorio_vendas.carregar_vendas()
    
    # mostra produtos
    print("\nProdutos disponíveis:")
    for produto in produtos:
        print(f"{produto.codigo} - {produto.nome} - Estoque: {produto.quantidade_estoque}")
    
    codigo = int(input("\nCódigo do produto: "))
    quantidade = int(input("Quantidade: "))
    
    # busca o produto
    produto_encontrado = None
    for produto in produtos:
        if produto.codigo == codigo:
            produto_encontrado = produto
            break
    
    if produto_encontrado == None:
        print("Produto não encontrado!")
        return
    
    # verifica estoque
    if produto_encontrado.quantidade_estoque < quantidade:
        print("Estoque insuficiente!")
        return
    
    # atualiza estoque
    produto_encontrado.quantidade_estoque = produto_encontrado.quantidade_estoque - quantidade
    
    # gera id da venda
    if len(vendas) > 0:
        maior_id = 0
        for v in vendas:
            if v.id > maior_id:
                maior_id = v.id
        novo_id = maior_id + 1
    else:
        novo_id = 1
    
    # cria venda
    venda = Venda(novo_id, produto_encontrado, quantidade, datetime.now())
    vendas.append(venda)
    
    # salva
    repositorio_produtos.salvar_produtos(produtos)
    repositorio_vendas.salvar_vendas(vendas)
    
    total = produto_encontrado.preco * quantidade
    print(f"Venda registrada! Total: R$ {total}")


def relatorio_estoque_baixo():
    limite = int(input("Limite de estoque baixo: "))
    produtos = relatorios.produtos_estoque_baixo(limite)
    
    print("\n=== PRODUTOS COM ESTOQUE BAIXO ===")
    for produto in produtos:
        print(f"{produto.codigo} - {produto.nome} - Estoque: {produto.quantidade_estoque}")


def relatorio_vendas_dia():
    data_str = input("Data (DD/MM/YYYY) ou deixe em branco para hoje: ")
    
    if data_str == "":
        data = datetime.now()
    else:
        data = datetime.strptime(data_str, "%d/%m/%Y")
    
    data_inicio = data.replace(hour=0, minute=0, second=0)
    data_fim = data.replace(hour=23, minute=59, second=59)
    
    total = relatorios.total_vendido_periodo(data_inicio, data_fim)
    
    print(f"\nTotal vendido: R$ {total}")


# programa principal
while True:
    opcao = menu_principal()
    
    if opcao == "1":
        while True:
            opcao_produto = menu_produtos()
            if opcao_produto == "1":
                cadastrar_produto()
            elif opcao_produto == "2":
                listar_produtos()
            elif opcao_produto == "0":
                break
    
    elif opcao == "2":
        while True:
            opcao_venda = menu_vendas()
            if opcao_venda == "1":
                registrar_venda()
            elif opcao_venda == "0":
                break
    
    elif opcao == "3":
        while True:
            opcao_relatorio = menu_relatorios()
            if opcao_relatorio == "1":
                relatorio_estoque_baixo()
            elif opcao_relatorio == "2":
                relatorio_vendas_dia()
            elif opcao_relatorio == "0":
                break
    
    elif opcao == "0":
        print("Até logo!")
        break