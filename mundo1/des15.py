days = int(input('Quantos dias alugados: '))
kms = float(input('Quantos kms rodados: '))
cald = (days*60) + (kms*0.15)
print(f'O total a pagar é: R${cald:.2f}')