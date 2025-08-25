# Faça um programa que calcule a soma entre todos o números ímpares que são multiplos de 3 e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i)
        soma += i
        cont += 1
print(f'a soma dos {cont} valores solicitados foi {soma}')
print('Acabou...')

# corrigido