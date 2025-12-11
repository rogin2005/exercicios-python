from random import randint

numero_usuario = int(input('Digite aqui um número para verificar se é igual ao número do pc: '))
print('O pc está pensando...')
sort = randint(0, 5)

if numero_usuario == sort:
    print('Parabéns vc acertou!')
else:
    print('Que pena vc errou')
    