# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
n = float(input('Digite a temperatura em °C para converté-la em °F: '))
f = (n*1.8) + 32
print(f'A temperatura de {n}°C é igual a {f:.1f}°F')