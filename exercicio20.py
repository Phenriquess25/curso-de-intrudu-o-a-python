
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

intersecao = conjunto1.intersection(conjunto2)

if len(intersecao) > 0:
    print("Há pelo menos um elemento em comum entre os conjuntos.")
    print("Elementos em comum:", intersecao)
else:
    print("Não há elementos em comum entre os conjuntos.")
