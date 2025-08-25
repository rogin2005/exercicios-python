# A confederação Nacional de natação  precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# -Até 9 anos: MIRIM / -Até 14 anos: INFANTIL / -Até 19 anos: JUNIOR / -Até 20 anos: SÊNIOR / -Acima: MASTER

import datetime

ano_atual = datetime.date.today().year

ano_nascimento = int(input('Digite seu ano de nascimento: '))

idade = ano_atual - ano_nascimento
print(f'Sua idade é: {idade}')

if idade <= 9:
    print('MIRIM')
elif idade >= 10 and idade <= 14:
    print('INFANTIL')
elif idade >= 15 and idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
else:
    print('MASTER')
    
# concluído...