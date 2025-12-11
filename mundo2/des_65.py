# Crie um programa que leia varios numeros inteiros pelo teclado. no final da execução, mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# metodo usando 0 para sair
'''num = int(input('Digite um valor qualquer ou 0 para sair: '))

numeros = 0
maior = num
menor = num
cont = 0
media = num

if num != 0:
    numeros += num
    cont += 1
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
        
while (num != 0):
    num = int(input('Digite mais algum valor ou 0 para sair: '))
    if num != 0:
        numeros += num
        cont += 1
        if num > maior:
            maior = num
        elif num < menor and num != 0:
            menor = num
    else:
        media = numeros / cont
        
print(f'Terminou, a média entre os valores foi {media}, o maior valor lido foi {maior} e o menor valor lido foi {menor}')'''

# metodo usando s ou n para prosseguir
num = int(input('Digite um número qualquer: '))
numeros = 0
maior = menor = media = num
mais = 'S'
while mais in 'Ss':
    numeros += 1
    if numeros > 1:
        num = int(input('Digite o numero: '))
        media += num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    mais = str(input('Deseja continuar digitando numeros? [S/N] ')).upper().strip()[0]
media = media / numeros
print(f'Encerrou. foram digitados {numeros} numeros o maior valor foi {maior}, o menor valor foi {menor} e a media entre os valores foi {media}')


# o metodo do guanabara ele basicamente só moveu os inputs para dentro do while assim deixando mais curto o programa dele...
'''resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    # lógica de calculo
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
# media
# prints finais...'''
