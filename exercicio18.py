def calcular_media_e_status(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(f"A média do aluno é: {media}")
    
    if media < 5:
        print("Situação: REPROVADO")
    elif media >= 5 and media < 7:
        print("Situação: RECUPERAÇÃO")
    else:
        print("Situação: APROVADO")
        
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

calcular_media_e_status(nota1, nota2)
