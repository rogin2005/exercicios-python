for i in range(5, 0, -1):
    print(i)
print('World!')

for c in range(0, 9):
    print("i'm idiot")
print('yes!')

for f in range(0, 11):
    print(f)
print('bye')

for x in range(10, 0, -1):
    print(x)
print('GOO!!!')

patos = int(input('Digite uma quantidade de patos: '))
for p in range(0, patos+1):
    print(f'{p} pato(s)')
print('acabou os patos:(')


nums = int(input('Digite um número para verificarmos o caminho até ele identificando números pares: '))
for i in range(1, nums+1):
    if i % 2 == 0:
        print(f'{i} é par')
    else:
        print(f'{i} é impar')
print('a contagem acabou...')


i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
for v in range(i, f+1, p):
    print(v)
print('CABOU-SE!!!')


somas = 0
for t in range(0, 5):
    ncp = int(input('Digite um número para somar: '))
    somas += ncp
print(f'A soma final é: {somas}')


