# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
mts = float(input('Digite um valor: '))
cms = mts * 100
mlts = mts * 1000
print(f'Valor em metros: {mts}m\nValor em centímetros: {cms}cm\nValor em milímetros: {mlts}mm') 


#-----------------------------------------------------------------
# Abaixo código ampliado que mostra todas as medidas a partir do metro

"""metros = float(input('Digite a qtd de metros: '))

km = metros * 0.001
hm = metros * 0.01
dam = metros * 0.1
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print(f'{metros:.1f}m\n{km:.3f}km\n{hm:.2f}hm\n{dam:.1f}dam\n{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm')"""
