# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print('números pares de 1 a 50...')
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
print('acabou...')

# método guanabara
"""for i in range(2, 51, 2):
    print(i)
print('acabou...')"""