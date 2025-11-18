while True:
    num = int(input('digite um número qualquer ou 0 pra sair: '))
    if num == 0:
        break
    if num % 2 == 0:
        print(f'{num} é par!')
    else:
        print(f'{num} é impar!')
print('o programa acabou!')