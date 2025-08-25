# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Olá, por favor digite o seu sexo[M/F]: ')).strip()
while sexo not in 'MmFf':
    sexo = str(input('Ops, parece que vc não digitou um sexo válido, tente novamente digitando "M" ou "F": '))

print(f'Sexo {sexo.upper()} registrado muito obrigado, vc é muito gentil!')
