# Tupla com nomes de produtos e preços
lista_produto = (
    ('Produto 1', 10.50),
    ('Produto 2', 19.50),
    ('Produto 3', 5.00),
    ('Produto 4', 15.30),
    ('Produto 5', 8.60)
)

# Exibindo a listagem de preços
print("LISTAGEM DE PREÇOS")
print("PRODUTO        | PREÇO")
for produto, preco in lista_produto:
    print(f"{produto.ljust(15)}| R${preco:.2f}")

