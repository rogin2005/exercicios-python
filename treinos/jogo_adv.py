# jogo de advinhação
from random import randint
print('SEJA BEM VINDO AO JOGO DE ADIVINHAÇÃO DO ROGIN!!!')
player = 0
while (player < 1) or (player > 10):
    player = int(input('Digite um número de 1 a 10: '))
pc = randint(1, 10)
tentativas = 1
pc_win = 0
while (player != pc):
    pc_win += 1
    player = 0
    while (player < 1) or (player > 10):
        player = int(input('Não é esse hein, tente novamente com um número de 1 a 10: '))
    tentativas += 1
print(f'Ebaaaa, você venceu com {tentativas} tentativas e o pc venceu {pc_win} vezes!')