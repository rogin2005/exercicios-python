# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5x4x3x2x1 = 120 (usando for)

num = int(input('Digite um número para ver o seu fatorial: '))

const_num = num
cont = 0

for i in range(num, 0, -1):
    if i == const_num:
        mult = num * (num - 1)
        cont += mult
    else:
        if num > 1:
            mult = cont * (num - 1)
            cont = 0
            cont += mult
    num -= 1
if const_num > 1:
    print(f'O fatorial de {const_num} é {cont}')
else:
    print(f'O fatorial de {const_num} é 1')
