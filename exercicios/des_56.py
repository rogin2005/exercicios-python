# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do grupo. - ok / Qual é o nome do homem mais velho. - ok / quantas mulheres tem menos de 20 anos. - ok

media_idade = 0
homem_v = ''
mulher_20 = 0
maior_im = 0

for i in range(1, 5):
    nome = input(f'nome da {i}° pessoa: ')
    idade = int(input(f'idade da {i}° pessoa: '))
    sexo = input(f'sexo da {i}° pessoa (m/f): ').upper()
    print('-'*30)
    if i < 5:
        media_idade += idade
    if sexo == 'M':
        maior_im = idade
        homem_v = nome
    elif idade > maior_im and sexo == 'M':
        maior_im = idade
        homem_v = nome
    if sexo == 'F' and idade < 20:
        mulher_20 += 1  
media_idade = media_idade / 4
print(f'média idade do grupo: {media_idade} anos')
print(f'homem mais velho do grupo tem {maior_im} anos e se chama {homem_v}.')
print(f'quantidade de mulheres que tem menos de 20 anos: {mulher_20}')


# lógica guanabara
"""somaidade = 0 
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'----- {p}° PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4"""
# prints finais...
