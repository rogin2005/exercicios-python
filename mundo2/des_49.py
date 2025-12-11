# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, so que agora utilizando um laço for.

print('-'*20, 'TABUADA DO ROJÃO', '-'*22)
num = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
    print(f'{num}x{i}={num*i}')

# corrigido