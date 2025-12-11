# faça um programa que jogue par ou impar com o computador. o jogo so será interrompido quando o jogador perder. mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

from random import randint

print('/'*30)
print('Jogo de Ímpar ou Par!')
print('\\'*30)
jogador = pc = vitorias = calculo = 0
escolha = resultado = ''

while True:
    jogador = int(input('Digite um valor: '))
    escolha = str(input('Vc escolhe Par ou Ímpar? [P/I] ')).upper().strip()[0]
    pc = randint(1, 10)
    calculo = jogador + pc
    # logica par ou impar completa
    if calculo % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "ÍMPAR"
    # logica pra saber se o jogador ganhou ou não...
    if escolha in "PI":
        print('-'*30)
        print(f'Você jogou {jogador} e o pc jogou {pc}. Total de {calculo} DEU {resultado}')
        print('-'*30)
        if escolha == "P" and resultado == "PAR":
            print('Você VENCEU!', 'Vamos jogar novamente...')
            vitorias += 1
        elif escolha == "I" and resultado == "ÍMPAR":
            print('Você VENCEU!', 'Vamos jogar novamente...')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    else:
        print('Ops vc não digitou uma opção válida, tente novamente...')
    print('-='*15)
print(f'GAME OVER!  Você venceu {vitorias} vezes.')

# metodo guanabara
'''from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU IMPAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')'''