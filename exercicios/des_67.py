# Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. o programa será interrompido quando o numero solicitado for negativo.

num = 0
while True:
    num = int(input('Quer ver a tabuada de qual número? (digite um valor negativo para sair): '))
    if num < 0:
        break
    print('-'*30)
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    print('-'*30)
print('-'*30)
print('Tabuada encerrada. Volte sempre!')

# Corrigido, minha lógica foi igual do guanabara...