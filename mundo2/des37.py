# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1- para binário / 2- para octal / 3- para hexadecimal

numero = int(input('Digite um número qualquer: '))
menu = int(input('Selecione uma das opções abaixo para converter:\n1- Binário\n2- Octal\n3- Hexadecimal\n'))

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if menu == 1:
    print(f'Número em binário: {binario}')
elif menu == 2:
    print(f'Número em octal: {octal}')
elif menu == 3:
    print(f'Número em hexadecimal: {hexadecimal}')
else:
    print('Opção inválida tente novamente...')    
    
# Concluído...

"""# des 37...

num = int(input('Digite um número para converter: '))

print('Escolha para qual base deseja converter:\n1 - binário\n2 - octal\n3 - hexadecimal')
escolha = int(input('Sua escolha: '))

if escolha == 1:
    print(f'número em binário: {bin(num)}')
elif escolha == 2:
    print(f'número em octal: {oct(num)}')
elif escolha == 3:
    print(f'número em hexadecimal: {hex(num)}')
else:
    print('Escolha uma opção válida!')
"""