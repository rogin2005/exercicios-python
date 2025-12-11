salario = float(input('Digite o salário do seu funcionário: '))

if salario >= 1250:
    print(f'ganhava {salario} aumento de 10%: R${salario*1.10:.2f}')
else:
    print(f'ganhava {salario} aumento de 15%: R${salario*1.15:.2f}')