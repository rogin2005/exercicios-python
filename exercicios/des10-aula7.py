# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. (Considere US$1,00 = R$5,60)
din = float(input('Digite quantos Reais vc tem: '))
calc = din / 5.60
print(f'Vc pode comprar US${calc:.2f}')