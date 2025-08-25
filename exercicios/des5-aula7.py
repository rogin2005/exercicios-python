# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n1 = int(input('Digite aqui um valor: '))
ant = n1 - 1
suc = n1 + 1
print('Este é o antecessor do valor digitado: {}\nEste é o sucessor do valor digitado: {}'.format(ant, suc))