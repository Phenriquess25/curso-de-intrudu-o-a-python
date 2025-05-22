nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota2: "))
media = nota1 + nota2 / 2

if media >= 5.0:
    print("Parabéns, você foi aprovado media: {:.1f}".format(media))
else:
    print("Você foi reprovado media: {:.1f}".format(media))
