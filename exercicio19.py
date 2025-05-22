
agenda = {}


def incluir_novo_nome(nome, telefones):
    if nome not in agenda:
        agenda[nome] = telefones
    else:
        agenda[nome].extend(telefones)


def incluir_telefone(nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
    else:
        resposta = input(
            f'O nome "{nome}" não existe na agenda. Deseja incluí-lo? (s/n): ')
        if resposta.lower() == 's':
            incluir_novo_nome(nome, [telefone])
        else:
            print('Nome não incluído.')


def excluir_telefone(nome, telefone):
    if nome in agenda:
        if telefone in agenda[nome]:
            agenda[nome].remove(telefone)
            if not agenda[nome]:
                del agenda[nome]
                print(
                    f'Todos os telefones de {nome} foram removidos. {nome} foi excluído da agenda.')
            else:
                print(f'Telefone {telefone} removido de {nome}.')
        else:
            print(f'O telefone {telefone} não está associado a {nome}.')
    else:
        print(f'{nome} não encontrado na agenda.')


def excluir_nome(nome):
    if nome in agenda:
        del agenda[nome]
        print(f'{nome} foi excluído da agenda.')
    else:
        print(f'{nome} não encontrado na agenda.')


def consultar_telefone(nome):
    if nome in agenda:
        return agenda[nome]
    else:
        return f'{nome} não encontrado na agenda.'

while True:
    print("\n### MENU ###")
    print("1. Incluir novo nome")
    print("2. Incluir telefone")
    print("3. Excluir telefone")
    print("4. Excluir nome")
    print("5. Consultar telefone")
    print("6. Sair")

    escolha = input("Escolha uma opção (1-6): ")

    if escolha == '1':
        nome = input("Digite o nome a ser incluído: ")
        telefones = input(
            "Digite os telefones (separados por espaço): ").split()
        incluir_novo_nome(nome, telefones)
    elif escolha == '2':
        nome = input("Digite o nome para adicionar telefone: ")
        telefone = input("Digite o telefone a ser incluído: ")
        incluir_telefone(nome, telefone)
    elif escolha == '3':
        nome = input("Digite o nome para excluir telefone: ")
        telefone = input("Digite o telefone a ser excluído: ")
        excluir_telefone(nome, telefone)
    elif escolha == '4':
        nome = input("Digite o nome a ser excluído: ")
        excluir_nome(nome)
    elif escolha == '5':
        nome = input("Digite o nome para consultar telefone: ")
        print(consultar_telefone(nome))
    elif escolha == '6':
        print("Encerrando o programa...")
        break
    else:
        print("Escolha inválida. Por favor, escolha uma opção de 1 a 6.")
