mais18 = 0
homens = 0
mulheres20 = 0

while True:
    idade = int(input("digite sua idade: "))
    sexo = input("digite seu sexo(M/F): ").upper()
    if idade > 18:
        mais18 += 1
        
    if sexo == 'M':
        homens += 1
        
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    
    continuar = input("deseja cadastrar mais alguem?(S/N): ").upper()
    if continuar != 'S':
        break
    
print(f"pessoas com mais de 18 anos: {mais18}")
print(f"quantidade de homens cadastrados: {homens}")
print(f"mulheres cadastradas com menos de 20 anos: {mulheres20}")
        