# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: "-O primeiro valor é maior" / "O segundo valor é maior" / "Não existe valor maior, os dois são iguais"

from time import sleep

val_1 = int(input('Digite o primeiro valor: '))
val_2 = int(input('Digite o segundo valor: '))

print('Calculando...')
sleep(2)

if val_1 > val_2:
    print('O primeiro valor é maior')
elif val_2 > val_1:
    print('O segundo valor é maior')
elif val_1 == val_2:
    print('Não existe valor maior, os dois são iguais')
    
# Concluído...