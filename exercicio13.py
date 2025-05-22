
palavras = ('ufal', 'python', 'pedro', 'telefone')
def encontrar_vogais(palavra):
    vogais = [letra for letra in palavra if letra in 'aeiou']
    return vogais

for palavra in palavras:
    vogais_encontradas = encontrar_vogais(palavra)
    print(f'Vogais de: ({palavra}) {vogais_encontradas}')
