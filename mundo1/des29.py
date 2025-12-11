carro = float(input('digite aqui a velocidade que o carro passou no radar: '))
print('analisando as condições...')
if carro > 80:
    print('vc foi multado! por ultrapassar o limite de 80km/h')
    multa = (carro-80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
print('tenha um ótimo dia e dirija com segurança.')