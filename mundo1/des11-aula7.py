# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
alt = int(input('Digite a altura da sua parede: '))
lar = int(input('Digite a largura da sua parede: '))
calc = alt * lar
tint = calc / 2
print(f'Sua parede tem {calc} metros quadrados e precisa de {tint} litros de tinta para ser completamente pintada.')
