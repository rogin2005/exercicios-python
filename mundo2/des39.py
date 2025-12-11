""" 
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

import datetime

ano_nascimento = int(input('Digite o ano do seu nascimento: '))

data_atual = datetime.date.today().year
idade = data_atual - ano_nascimento
qtd_anos = 18

if idade == qtd_anos:
    print('Já é hora de se alistar!')
elif idade < qtd_anos:
    print(f'Ainda não está no tempo de se alistar faltam {qtd_anos - idade} anos')
else:
    print(f'Já passou o tempo de se alistar, passaram-se {idade - qtd_anos} anos')

# Concluído