# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('-'*10, 'Progressão Aritmética', '-'*10)
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print(primeiro)

termos = primeiro

for i in range(1, 10):
    termos += razao
    print(termos)
    
    
# metodo guanabara
"""primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c} ', end='→ ')
print('ACABOU')"""