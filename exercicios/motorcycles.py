# adicionando item na lista
'''motorcycles = ['honda', 'bmw', 'yamaha']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)'''

# adicionando item na lista com .append()
'''motorcycles1 = ['honda', 'yamaha', 'suzuki']
print(motorcycles1)

motorcycles1.append('ducati')
print(motorcycles1)'''

# adicionando itens com .append() e insert() e removendo itens com del. o .append() adiciona itens no final da lista e o .insert() adiciona itens de acordo com o index desejado, por exemplo lista.insert(0, 'alguma coisa') aqui eu inseri uma string na primeira posição da lista.
'''motorcycles2 = []

motorcycles2.append('honda')
motorcycles2.append('bmw')
motorcycles2.append('suzuki')

print(motorcycles2)

motorcycles2.insert(0, 'yamaha')
print(motorcycles2)

del motorcycles2[0]
print(motorcycles2)

del motorcycles2[1]
print(motorcycles2)'''

# trabalhando com o método pop(), ele remove o último item da lista e guarda esse item, ou seja podemos armazenar esse item em uma variável por exemplo para exibir depois, seria útil por exemplo em um cenário onde temos informações que serão removidas, mas ainda precisaremos exibir elas em algum momento, assim não perdendo totalmente aquela informação...
motorcycles3 = ['honda', 'yamaha', 'suzuki']
print(motorcycles3)

popped_motorcyle = motorcycles3.pop()
print(motorcycles3)
print(popped_motorcyle)

