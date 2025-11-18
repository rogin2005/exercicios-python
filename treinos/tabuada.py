# tabuada que mostra as 10 primeiras multiplicações de um determinado número
num = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
    print(f'{num} x {i} = {num*i}')