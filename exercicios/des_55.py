# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []

for i in range(0, 5):
    peso = float(input('Digite o seu peso(kg): '))
    pesos.append(peso)
print(f'maior peso: {max(pesos)}kg')
print(f'menor peso: {min(pesos)}kg')


# método guanabara
"""maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'peso da {p}° pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}Kg')
print(f'O menor peso lido foi {menor}Kg')"""
