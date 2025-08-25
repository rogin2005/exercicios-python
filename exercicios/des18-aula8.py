# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang_graus = float(input('Digite aqui o ângulo: '))
ang_radianos = math.radians(ang_graus)
sen = math.sin(ang_radianos)
cos = math.cos(ang_radianos)
tan = math.tan(ang_radianos)
print(f'Seno: {sen:.2f} Cosseno: {cos:.2f} Tangente: {tan:.2f}')