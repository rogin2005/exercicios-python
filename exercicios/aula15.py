cont = 0
while cont <= 10:
    print(cont, end=' ')
    cont += 1

n = soma = 0    
while True:
    n = int(input('Digite um numero qualquer (-1 para parar):'))
    if n == -1:
        break
    soma += n
print(f'A soma deu {soma}')
    

