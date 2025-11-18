# calculadora de idade
from datetime import datetime
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = datetime.today().year
idade = ano_atual - ano_nascimento
print(f'Sua idade é {idade} anos!')