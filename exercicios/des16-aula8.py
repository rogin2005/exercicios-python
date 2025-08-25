""" 
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua posição Inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""
import math
num = float(input('Digite um número real com ponto flutuante: '))
print(f'O valor digitado foi: {num} a sua parte inteira é igual a: {math.trunc(num)}')

# dá pra fazer também com o método:
# from math import trunc
# aí você irá apenas tirar o "math." antes do trunc, e a funcionalidade irá agir da mesma forma.

# também tem outro método pra fazer que é usando "int(num)" no lugar de "math.trunc(num)"

# outra maneira é pegar o input e add o ":.0f"