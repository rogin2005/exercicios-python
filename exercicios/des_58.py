# melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

pc = randint(0, 10)

jogador = int(input("""Olá jogador Seja bem vindo ao jogo de adivinhação contra o computador!
nosso computador já pensou em um número de 0 a 10, faça o seu palpite: """))
tentativas = 1

while jogador != pc:
    if pc > jogador:
        jogador = int(input('Ops, o pc pensou em um número maior, tente novamente: '))
    else:
        jogador = int(input('Ops, o pc pensou em um número menor, tente novamente: '))
    tentativas += 1
print(f'Parabéns vc consigou acertar o número, vc usou exatamente {tentativas} tentativas!')


'''from random import randint
computador = randint(0, 10)
print('Sou seu computador... acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')'''
