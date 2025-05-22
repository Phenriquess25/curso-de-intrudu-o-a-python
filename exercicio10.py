numeros_extenso = {
    0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
    6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez', 11: 'onze',
    12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze', 16: 'dezesseis',
    17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte'
}

def mostrar_numero_extenso():
    while True:
        try:
            numero = int(input("Digite um número entre 0 e 20: "))
            if 0 <= numero <= 20:
                print(f"O número {numero} por extenso é: {numeros_extenso[numero]}")
                break
            else:
                print("Por favor, digite um número entre 0 e 20.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

mostrar_numero_extenso()
