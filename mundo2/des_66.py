# crie um programa que leia varios numeros inteiros pelo teclado. o programa so vai parar quando o usuario digitar o valor 999, que é a condição de parada. no final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = soma = numeros = 0
while True:
    num = int(input('Digite um número (999 pra parar): '))
    if num == 999:
        break
    soma += num
    numeros += 1
print(f'Acabou. foram digitados {numeros} numeros e a soma entre eles foi {soma}')

# logica do guanabara foi igual a minha, estou melhorando...