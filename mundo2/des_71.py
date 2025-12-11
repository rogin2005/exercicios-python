# Crie um programa que simule o funcionamento de um caixa eletronico. no inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('-'*30)
print('     BANCO DO ROJÃO ADMIN MASTER')
print('-'*30)
valor = int(input('Digite o valor que deseja sacar: R$'))
cont_50 = cont_20 = cont_10 = cont_1 = 0
while True:
    if valor >= 50:
        cont_50 += 1
        valor -= 50
    elif valor >= 20:
        cont_20 += 1
        valor -= 20
    elif valor >= 10:
        cont_10 += 1
        valor -= 10
    elif valor >= 1:
        cont_1 += 1
        valor -= 1
    else:
        break
if cont_50 > 0:
    print(f'No total {cont_50} cédulas de R$50')
if cont_20 > 0:
    print(f'No total {cont_20} cédulas de R$20')
if cont_10 > 0:
    print(f'No total {cont_10} cédulas de R$10')
if cont_1 > 0:
    print(f'No total {cont_1} cédulas de R$1')
print('-'*30)
print('Volte sempre no banco de ROJÃO ADMIN MASTER!!!')

# metodo guanabara
'''print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV! tenha um bom dia!')'''
