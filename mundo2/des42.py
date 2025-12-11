# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: -Equilátero: Todos os lado iguais / -Isósceles: dois lados iguais / -Escaleno: todos os lados diferentes

r1 = int(input('Digite o tamanho da primeira reta: '))
r2 = int(input('Digite o tamanho da segunda reta: '))
r3 = int(input('Digite o tamanho da terceira reta: '))

# Verificação se é equilátero
if r1 == r2 and r1 == r3 and r2 == r3:
    print('Triângulo Equilátero!')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1 and r1 != r2 and r1 != r3 and r2 != r3:
    print('Triângulo retângulo Escaleno!')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1 and r1 == r2 or r1 == r3 or r2 == r3:
    print('Triângulo retângulo Isósceles!')
else:
    print('Essas três retas não formam um triângulo...')

# Concluído...