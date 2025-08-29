# pegando o exercicio anterior da lista 2, vamos convidar só 5 convidados de início, após vamos informar que achamos uma mesa maior e vamos adicionar mais 3 pessoas na lista, com 3 instruções diferentes:
# 1 - com insert() para adicionar uma pessoa no inicio da lista
# 2 - com insert() para adicionar pessoa no meio da lista
# 3 - com append() para adicionar pessoa no final da lista

from time import sleep

convidados = ['Roger', 'Fabio', 'Lucas', 'Diego']
print(f'Olá {convidados[0]} venha para o jantar esta noite!')
print(f'Olá {convidados[1]} venha para o jantar esta noite!')
print(f'Olá {convidados[2]} venha para o jantar esta noite!')
print(f'Olá {convidados[3]} venha para o jantar esta noite!')
sleep(2)

print('\nBoa notícia, achei uma mesa maior e irei chamar mais pessoas para o jantar...')
sleep(2)

# inicio
convidados.insert(0, 'Zezinho')
# meio
convidados.insert(2, 'Tiago')
# final
convidados.append('Gustavo')

print('\nnova lista de convites:')
print(f'Olá {convidados[0]} venha para o jantar esta noite!')
print(f'Olá {convidados[1]} venha para o jantar esta noite!')
print(f'Olá {convidados[2]} venha para o jantar esta noite!')
print(f'Olá {convidados[3]} venha para o jantar esta noite!')
print(f'Olá {convidados[4]} venha para o jantar esta noite!')
print(f'Olá {convidados[5]} venha para o jantar esta noite!')
print(f'Olá {convidados[6]} venha para o jantar esta noite!')
