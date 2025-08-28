# usando a mesma lista de convidados do primeiro exercicio vamos considerar que um dos convidados não poderá comparecer, então vamos exibir ele e remover da lista, adicionando outro convidado na posição que ele estava na lista.

from time import sleep

convidados = ['Roger', 'Diego', 'Mikael', 'Camila']
print(f'Olá {convidados[0]} venha ao jantar esta noite!')
print(f'Olá {convidados[1]} venha ao jantar esta noite!')
print(f'Olá {convidados[2]} venha ao jantar esta noite!')
print(f'Olá {convidados[3]} venha ao jantar esta noite!')

print(f'\nOps, tivemos a triste notícia que {convidados[2]} não poderá comparecer, iremos substituir ele...')
print('Um momento, estamos alterando a lista...\n')
sleep(2)
del convidados[2]
convidados.insert(2, 'João')

print('nova lista de convidados:')
print(f'Olá {convidados[0]} venha ao jantar esta noite!')
print(f'Olá {convidados[1]} venha ao jantar esta noite!')
print(f'Olá {convidados[2]} venha ao jantar esta noite!')
print(f'Olá {convidados[3]} venha ao jantar esta noite!')
