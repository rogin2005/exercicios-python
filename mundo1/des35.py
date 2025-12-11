r1 = int(input('tamanho primeira reta: '))
r2 = int(input('tamanho segunda reta: '))
r3 = int(input('tamanho terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Essas Três retas podem formar um triângulo!')
else:
    print('Essas Três retas não podem formar um triângulo!')