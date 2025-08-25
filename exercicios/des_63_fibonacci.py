# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci. Ex: 0, 1, 1, 2, 3, 5, 8...

n = int(input('Digite quantos números da sequencia de fibonacci vc quer ver: '))

termo_1 = 0
termo_2 = 1
cont = n
t3 = False

if cont == 1:
    print(f'{termo_1}')
    cont -= 1
elif cont == 2:
    print(f'{termo_1}, {termo_2}')
    cont -= 2
elif cont >= 3:
    print(f'{termo_1}, {termo_2}, {termo_2},', end='')
    cont -= 3
    t3 = True
    termo_1 = termo_2


while (cont != 0):
    if t3:
        soma4 = termo_1 + termo_2
        termo_1 = termo_2
        termo_2 = soma4
        print(f' {soma4},', end='')
        cont -= 1
print(' ...')
print('Acabou!!!')

# Metodo guanabara
'''print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1}, {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f', {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(', FIM')
print('~'*30)'''