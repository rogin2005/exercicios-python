# contador regressivo até 0
num = 0
while num < 1:
    num = int(input('Digite um número maior que 0 para fazermos a contagem: '))
for i in range(num, -1, -1):
    print(f'{i} -> ', end='')
print('💥')