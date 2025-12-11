# Exercício muito interessante sobre como otimizar um programa...
alunos = [
    {"nome": input('Nome do primeiro aluno: '), "nota": float(input('Nota do primeiro aluno: '))},
    {"nome": input('Nome do segundo aluno: '), "nota": float(input('Nota do segundo aluno: '))},
    {"nome": input('Nome do terceiro aluno: '), "nota": float(input('Nota do terceiro aluno: '))},
    {"nome": input('Nome do quarto aluno: '), "nota": float(input('Nota do quarto aluno: '))}
]
for aluno in alunos:
    if aluno["nota"] >= 7.0:
        print(f'Parabéns {aluno["nome"]}, sua nota foi {aluno["nota"]}, vc passou com excelência!')
    elif 6.0 <= aluno["nota"] <= 6.9:
        print(f'Está de recuperação {aluno["nome"]}, sua nota foi {aluno["nota"]}')
    else:
        print(f'Está reprovado {aluno["nome"]}, sua nota foi {aluno["nota"]}')