pessoas = []
while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
    if nome == 'sair':
        break
    peso = float(input("Digite o peso da pessoa: "))
    pessoas.append({'nome': nome, 'peso': peso})
    
quantidade_pessoas = len(pessoas)
print(f"\nForam cadastradas {quantidade_pessoas} pessoa(s).")

pessoas_ordenadas_peso_desc = sorted(pessoas, key=lambda x: x['peso'], reverse=True)
print("\nPessoas mais pesadas:")
for pessoa in pessoas_ordenadas_peso_desc:
    print(f"{pessoa['nome']} - Peso: {pessoa['peso']} kg")
    
pessoas_ordenadas_peso_asc = sorted(pessoas, key=lambda x: x['peso'])
print("\nPessoas mais leves:")
for pessoa in pessoas_ordenadas_peso_asc:
    print(f"{pessoa['nome']} - Peso: {pessoa['peso']} kg")
