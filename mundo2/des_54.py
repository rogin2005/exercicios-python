# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. Maioridade: 21 anos

from datetime import date
ano_atual = date.today().year
print(f'ano atual: {ano_atual}')

cont_maior = 0
cont_menor = 0

for i in range(0, 7):
    ano_nas = int(input('Digite seu ano de nascimento: '))
    idade = ano_atual - ano_nas
    print(f'sua idade: {idade}')
    if idade >= 21:
        print('Vc é maior de idade!')
        cont_maior += 1
    else:
        print('Vc é menor de idade!')
        cont_menor += 1
        
print(f'quantidade de maiores de idade: {cont_maior}')
print(f'quantidade de menores de idade: {cont_menor}')

# corrigido
# o metodo do guanabara desta vez foi parecido com o meu, apenas com diferenças não tão relevantes em alguns prints e no input principal, mas os resultados foram os mesmos.