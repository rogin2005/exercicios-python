# Crie um programa que leia vários números inteiros pelo teclado. o programa so vai parar quando o usuario digitar o valor 999, que é a condição da parada. no final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag que é o 999)

valor = int(input('Digite um valor inteiro qualquer ou o número 999 para sair do programa: '))

numeros = 0
soma = 0

if valor != 999:
    numeros += 1
    soma += valor

while valor != 999:
    valor = int(input('Digite mais algum valor se deseja continuar ou 999 para sair: '))
    if valor != 999:
        numeros += 1
        soma += valor
print(f'Encerrou foram digitados {numeros} numeros e a soma entre eles foi {soma}')

# método guanabara
'''num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))
print(f'Você digitou {cont} numeros e a soma entre eles foi {soma}.')'''