# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

casa = float(input('Qual o valor da casa que deseja comprar? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos pretende pagar? '))

print('Um momento, estamos calculando se seu empréstimo será aprovado...')
sleep(3)


prestacao_mensal = anos * 12
print(f'Total de parcelas: {prestacao_mensal}')

valor_parcela = casa / prestacao_mensal
print(f'O valor da parcela fica: {valor_parcela:.2f}')

porcentagem_salario = salario * 0.30

if valor_parcela <= porcentagem_salario:
    print('Parabéns, seu empréstimo foi aprovado!!!')
else:
    print('Que pena seu empréstimo não foi aprovado...')

#concluído!

"""# (Des-36) Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

print('Seja bem vindo ao banco Bela Vista!!!')

casa = float(input('Qual o valor da casa que vc deseja? '))
salario = float(input('Qual seu salário mensal atualmente? '))
anos = int(input('em quantos anos pretende pagar? '))

print('Um momento estamos calculando seu empréstimo...')
sleep(3)

meses = anos * 12
prestacao_mensal = casa / meses
percent_salario = salario * 0.30

if prestacao_mensal <= percent_salario:
    print('Parabéns seu empréstimo foi aprovado!!!')
    print(f'Serão {meses} parcelas de R${prestacao_mensal:.2f}')
else:
    print('Ah que pena, não conseguimos concluir seu empréstimo, tente novamente em 3 meses ou com uma casa diferente...')

"""