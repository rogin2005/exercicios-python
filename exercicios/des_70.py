# crie um programa que leia o nome e o preço de vários produtos. o programa deverá perguntar se o usuario vai continuar. no final, mostre: a) Qual é o total gasto na compra. b) Quantos produtos custam mais de R$1.000. c)Qual é o nome do produto mais barato.

preco = mil = total = menor = cont = 0
pergunta = barato = produto = ''
print('='*30)
print('     LOJA DO ROJÃO ADS')
print('='*30)
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = int(input('Preço do produto: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        mil += 1
    if cont == 1:
        menor = preco
        barato = produto
    if preco < menor:
        menor = preco
        barato = produto
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while pergunta not in "SN":
        pergunta = str(input('Quer continuar? S ou N: ')).upper().strip()[0]
    if pergunta == "N":
        break
print('-'*10, "FIM DO PROGRAMA", '-'*10)
print(f'Total da compra foi R${total:.2f}')
print(f'Temos {mil} produtos acima de R$1000.00')
print(f'O produto mais barato é {barato} e custa R${menor:.2f}')    

# usei uma logica parecida com a do gunabara, mas ele trouxe uma simplificação de codigo muito boa que ao inves de verificar o cont == 1 e se o preco for menor do q o menor a gente pode fazer isso em um if só com "if cont == 1 or preco < menor" isso deixa mais conciso, no demais nossa logica foi bem parecida...
