pesos = []
for x in range(5):
    peso = float(input(f"digite seu peso {x + 1}: "))
    pesos.append(peso)
    
maiorpeso = max(pesos)
menorpeso = min(pesos)

print(f"O maior peso lido foi: {maiorpeso}kg")
print(f"o menor peso lido foi: {menorpeso}kg")
