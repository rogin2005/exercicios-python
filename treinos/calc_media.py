# calcular média
from time import sleep
qtdalunos = int(input('Quantos alunos terão a média calculada: '))
cont = 0
alunos = []
medias = []
while cont != qtdalunos:
    aluno = input(f'Informe o nome do {cont+1}° aluno: ')
    n1 = int(input(f'Primeira nota do {aluno}: '))
    n2 = int(input(f'Segunda nota do {aluno}: '))
    n3 = int(input(f'Terceira nota do {aluno}: '))
    media = (n1 + n2 + n3) / 3
    alunos.append(aluno)
    medias.append(media)
    cont += 1
    print('Contabilizando só um momento...')
    sleep(2)

for aluno, media in zip(alunos, medias):
    if media >= 7:
        status = 'APROVADO'
    else:
        status = 'REPROVADO'
    print(f'O aluno {aluno} tem a media {media} ele está {status}!')
    print('processando...')
    sleep(2)
print('O programa terminou!')