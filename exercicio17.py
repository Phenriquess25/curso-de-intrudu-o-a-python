def aplicar_aumento(salario):
    if salario > 1250.00:
        aumento = salario * 0.10  
    else:
        aumento = salario * 0.15  
        
    salario_com_aumento = salario + aumento
    return salario_com_aumento

salario_funcionario = float(input("Digite o salário do funcionário: "))
salario_com_aumento = aplicar_aumento(salario_funcionario)
print(f"O salário com aumento é: R${salario_com_aumento:.2f}")
