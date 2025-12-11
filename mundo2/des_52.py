# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))

contador = 0

for i in range(num, 0, -1):
    if num % i == 0:
        contador += 1
print(f'contador: {contador}')
        
if contador == 2:
    print(f'{num} é primo!')
else:
    print(f'{num} não é primo!')
    

# metodo guanabara
"""num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')
print(f'\n\033[mO número {num} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')"""