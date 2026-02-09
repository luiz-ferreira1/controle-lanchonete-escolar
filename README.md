# Projeto F- Controle de Estoque da Lanchonete Escolar

Sistema simples para gerenciar estoque e vendas de uma lanchonete escolar.

## Execução do projeto

Basta rodar no vscode ou em alguma IDE para python. Os comandos com opções para o controle de estoque
aparecerão no terminal de comando.



## Estrutura

```
lanchonete_simples/
-main.py                    # Programa principal com menus
-models.py                  # Classes Produto e Venda
-repositorio_produtos.py    # Funções para produtos
-repositorio_vendas.py      # Funções para vendas
-relatorios.py              # Funções de relatórios
-data/
    -produtos.csv           # Dados dos produtos
    -vendas.csv             # Dados das vendas
```

## Funcionalidades

### Produtos
- Cadastrar produto (nome, preço, quantidade)
- Listar produtos

### Vendas
- Registrar venda
- Atualiza estoque automaticamente
- Não permite estoque negativo

### Relatórios
- Produtos com estoque baixo
- Total vendido no dia

## Classes

### Produto
- codigo
- nome
- preco
- quantidade_estoque

### Venda
- id
- produto (objeto Produto - **relação entre objetos**)
- quantidade
- data

## Relação entre Objetos

A classe **Venda** tem um atributo **produto** que é um objeto da classe **Produto**.
Isso cria uma relação de composição entre as classes.