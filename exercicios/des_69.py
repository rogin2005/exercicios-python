# crie um programa que leia a idade e o sexo de varias pessoas. a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. no final, mostre: a) quantas pessoas tem mais de 18 anos. b) Quantos homens foram cadastrados. c) Quantas mulheres tem menos de 20 anos.

idade = pessoas_18 = homens = mulheres_20 = 0
sexo = pergunta = ''

print('='*30)
print('     CADASTRO DE PESSOAS')
print('='*30)

while True:
    print('='*30)
    print('     CADASTRE UM INDIVIDUO')
    print('='*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in "MF":
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('='*30)
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while pergunta not in "SN":
        pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if idade >= 18:
        pessoas_18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres_20 += 1
    if pergunta == 'N':
        break
print('-'*30)
print('FIM DO PROGRAMA!')
print(f'''Pessoas com mais de 18 anos: {pessoas_18}
Homens cadastrados: {homens}
Mulheres com menos de 20 anos: {mulheres_20}
      ''')

# tive uma lógica muito parecida com a do guanabara, com apenas poucas diferenças em alguns poucos metodos, mas tivemos um resultado parecido...
