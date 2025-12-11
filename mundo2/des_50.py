# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o

somas = 0
cont = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}° número inteiro: '))
    if num % 2 == 0:
        somas += num
        cont += 1
print(f'vc informou {cont} número(s) par(es) e a soma entre eles foi: {somas}')

# corrigido