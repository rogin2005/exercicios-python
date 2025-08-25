# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome do escolhido.
import random

a1 = str(input('primeiro aluno: '))
a2 = str(input('segundo aluno: '))
a3 = str(input('terceiro aluno: '))
a4 = str(input('quarto aluno: '))

lista_alunos = [a1, a2, a3, a4]

print(f'O escolhido foi {random.choice(lista_alunos)}')