# lista de convidados anterior, informar que a mesa não virá a tempo, remover convidados e exibir msg até ficar so 2, msg para os ultimos 2 convidados, deletar os ultimos 2 e mostrar a lista vazia

convidados = ['t1', 't2', 't3', 't4', 't5']

for conv in convidados:
    print(f'Olá {conv} hoje a noite terá um jantar!')
print('que pena, nossa mesa grande não chegará a tempo, só poderemos convidar duas pessoas.')
p1 = convidados.pop()
print(f'sinto muito em não poder lhe convidar {p1}')
p2 = convidados.pop()
print(f'sinto muito em não poder lhe convidar {p2}')
p3 = convidados.pop()
print(f'sinto muito em não poder lhe convidar {p3}')
for c in convidados:
    print(f'Ficamos felizes em poder lhe convidar {c}')
del convidados[0]
del convidados[0]
print('lista vazia:',convidados)
