class Pais:
    def __init__(self, nome, capital, dimensao_km2, populacao):
        self.nome = nome
        self.capital = capital
        self.dimensao_km2 = dimensao_km2
        self.populacao = populacao

    @property
    def densidade_populacional(self):
        return self.populacao / self.dimensao_km2

    def obter_densidade_populacional(self):
        return self.densidade_populacional

    def __str__(self):
        return f"País: {self.nome}\nCapital: {self.capital}\nDimensão: {self.dimensao_km2} km²\nPopulação: {self.populacao}"


def criar_pais():
    nome = input("Digite o nome do país: ")
    capital = input("Digite o nome da capital: ")
    dimensao_km2 = float(input("Digite a dimensão do país em km²: "))
    populacao = int(input("Digite a população do país: "))
    return Pais(nome, capital, dimensao_km2, populacao)


paises = []

while True:
    print("\n### MENU ###")
    print("1. Adicionar país")
    print("2. Mostrar países e suas densidades populacionais")
    print("3. Sair")

    escolha = input("Escolha uma opção (1-3): ")

    if escolha == '1':
        novo_pais = criar_pais()
        paises.append(novo_pais)
        print("País adicionado com sucesso!")
    elif escolha == '2':
        if not paises:
            print("Nenhum país adicionado ainda.")
        else:
            print("\n### PAÍSES E SUAS DENSIDADES POPULACIONAIS ###")
            for pais in paises:
                print(pais)
                print("Densidade Populacional:",
                      pais.obter_densidade_populacional(), "habitantes por km²")
    elif escolha == '3':
        print("Encerrando o programa...")
        break
    else:
        print("Escolha inválida. Por favor, escolha uma opção de 1 a 3.")
