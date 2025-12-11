# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
catop = float(input('Digite aqui o comprimento do cateto oposto: '))
catadj = float(input('Digite aqui o comprimento do cateto adjacente: '))
hipot = math.hypot(catop, catadj)
print(f'Resultado: {hipot:.2f}')

