# cod 1: métodos de lista
cars = ['horizonte', 'tuvalu', 'zurique', 'fortaleza', 'baturite', 'aratuba']
print(cars)
print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))
print(cars)
cars.reverse()
print(cars)
cars.reverse()
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# cod 2: métodos de lista
coisas = ['fortaleza', 'goias', 'turquia', 'frança', 'titan', 'bros', 'gol', 'opala', 'roma', 'cairo']
print(f'na lista temos {len(coisas)} coisas')
print(sorted(coisas))
print(sorted(coisas, reverse=True))
coisas.sort()
print(coisas)
coisas.sort()
print(coisas)
coisas.sort(reverse=True)
print(coisas)
coisas.sort(reverse=True)
print(coisas)
coisas.reverse()
print(coisas)
coisas.reverse()
print(coisas)

# cod 3: append de lista
squares = []
for i in range(1,11):
    squares.append(i**2)
    
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

# cod 4: list comprehension
squares = [valor**2 for valor in range(1,11)]
print(squares)

# cod 5: list comprehension
cubos = [print(i**3) for i in list(range(1,11))]

# cod 6: lista copiada
my_pizzas = ['feijão', 'macarrão', 'torta', 'Uva']
friend_pizzas = my_pizzas[:]
my_pizzas.append('sorvete')
friend_pizzas.append('tamarindo')
print('As minhas pizzas favoritas são:')
for item in my_pizzas:
    print(item)
print('As pizzas favoritas do meu amigo são')
for item in friend_pizzas:
    print(item)

# cod 7: tupla
comidas = ('Arroz', 'Caranguejo', 'lasanha', 'macarrão', 'lagosta')
print('Cardápio do restaurante: ')
for comida in comidas:
    print(comida)
#comidas[0] = 'Batata'
comidas = ('Caviar', 'Arroz grego', 'tomate', 'vinagre', 'farinha')
print('\nNovo cardápio do restaurante: ')
for comida in comidas:
    print(comida)

