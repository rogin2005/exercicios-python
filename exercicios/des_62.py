# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

p_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('Mostrando os 10 primeiros termos dessa PA...')
cont = 0
ult_termo = 0
print(f'{p_termo}, ', end='')
while (cont != 10):
    cont += 1
    if cont < 10:
        p_termo += razao
        print(f'{p_termo}, ', end='')
    else:
        print('...')
        ult_termo = p_termo
print(f'os 10 primeiros termos acabaram...')
p_termo = int(input('Se desejar pode digitar a quantidade de termos a mais que quer ver ou digite 0 para sair: '))
while (p_termo != -1):
    if p_termo > 1:
        ult_termo += razao
        print(f'{ult_termo}, ', end='')
        cont += 1
    elif p_termo == 1:
        ult_termo += razao
        print(f'{ult_termo}, ...')
        cont += 1
    else:
        p_termo = int(input('Se ainda deseja ver mais algum termo da razão só digitar a quantidade ou 0 para sair: '))
        if p_termo != 0:
            p_termo += 1
    p_termo -= 1
print(f'A progressão terminou, foram exibidos {cont} termos.')
print('Tchau...')


# metodo guanabara
'''print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}, ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')'''
