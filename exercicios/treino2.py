meta = int(input('Defina uma meta em reais que vc deseja alcançar: '))
din = int(input('Digite aqui quanto vc quer aplicar por mês: '))
mes = int(input('Digite aqui por quantos meses vc pretende aplicar esse dinheiro: '))
mult = din * mes
if mult >= meta:
    print(f'Esta previsão está correta, em {mes} meses vc irá alcançar sua meta.')
else:
    print('Infelizmente com essa previsão vc não irá alcançar sua meta...')