def radar(velocidade_carro, limite_velocidade):
    if velocidade_carro <= limite_velocidade:
        return "Você está dentro dos parâmetros da lei, tenha um bom dia!"
    else:
        diferenca = velocidade_carro - limite_velocidade
        multa = diferenca * 7
        return f"Ultrapassou o limite de velocidade em {diferenca} km/h. Deve pagar uma multa de R${multa:.2f}."

velocidade_carro = float(input("Digite a velocidade do carro (em km/h): "))
limite_velocidade = float(input("Digite o limite de velocidade (em km/h): "))

resultado = radar(velocidade_carro, limite_velocidade)
print(resultado)

