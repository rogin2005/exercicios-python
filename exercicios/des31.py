distancia = float(input('Digite a distância percorrida: '))

if distancia > 0 and distancia < 201:
    print(f'Sua corrida deu R${distancia * 0.50:.2f}')
elif distancia >= 201:
    print(f'Sua corrida deu R${distancia * 0.45:.2f}')
else:
    print('ops digite um número maior q zero...')