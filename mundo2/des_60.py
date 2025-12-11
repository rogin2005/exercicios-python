# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5x4x3x2x1 = 120 (usando while)

from math import factorial

num = int(input('Olá, digite um número qualquer para ver seu fatorial: '))

const_num = num
cont = 0

while (num > 0):
    if cont == 0:
        calc = num * (num - 1)
        cont += calc
    else:
        if num > 1:
            calc = cont * (num - 1)
            cont = 0
            cont = calc
    num -= 1
if const_num > 1:
    print(f'O fatorial de {const_num} é igual a {cont}')
else:
    print(f'O fatorial de {const_num} é igual a 1')


# método 1 usando math pelo guanabara
'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')'''

# método 2 guanabara hardcode kkk
'''n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')'''

