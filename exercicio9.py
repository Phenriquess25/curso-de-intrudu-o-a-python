valor_de_saque = int(input("digite o valor a ser sacado: R$"))

cedula_50 = cedula_20 = cedula_10 = moeda_1 = 0

while  valor_de_saque >= 50:
    valor_de_saque -= 50
    cedula_50 += 1

while valor_de_saque >= 20:
    valor_de_saque -= 20 
    cedula_20 += 1

while valor_de_saque >= 10:
    valor_de_saque -=10
    cedula_10 += 1

while valor_de_saque >=1:
    valor_de_saque -= 1
    moeda_1 += 1

print("quantidade de cedulas:")
print(f"R$50: {cedula_50}")
print(f"R$20: {cedula_20}")
print(f"R$10: {cedula_10}")
print(f"moedas de R$1: {moeda_1}")
