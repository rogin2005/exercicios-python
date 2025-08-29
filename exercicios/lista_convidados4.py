# vamos iniciar com o exercicio 3 anunciando as pessoas, porém vamos mudar por conta que a mesa não chegará a tempo então devemos mostrar uma mensagem informando que vamos remover várias pessoas, deixando só duas na lista vamos utilizar o método pop() e exibindo uma mensagem que sente muito pra cada pessoa que for removida, depois vamos mostrar a nova lista só com duas pessoas, e logo após vamos utilizar o método del para remover os últimos dois nomes da lista para garantir que tenha uma lista vazia e vamos exibir ela vazia.

from time import sleep

convidados = ['Roger', 'Gustavo', 'Mikael', 'Luiza', 'Fabio', 'Lucas', 'Hugo']
print(f'Olá {convidados[0]} venha para o jantar esta noite!')
print(f'Olá {convidados[1]} venha para o jantar esta noite!')
print(f'Olá {convidados[2]} venha para o jantar esta noite!')
print(f'Olá {convidados[3]} venha para o jantar esta noite!')
print(f'Olá {convidados[4]} venha para o jantar esta noite!')
print(f'Olá {convidados[5]} venha para o jantar esta noite!')
print(f'Olá {convidados[6]} venha para o jantar esta noite!')
sleep(2)

print('\nUma péssima notícia, nossa mesa de jantar não irá chegar a tempo, infelizmente só vamos poder convidar 2 pessoas para o jantar...\n')
