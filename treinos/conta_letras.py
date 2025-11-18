# conta caracteres
palavra = str(input('Digite uma palavra qualquer: ')).strip()
carac = 0
for i in palavra:
    if i != ' ':
        carac += 1
print(f'analisando a palavra tem {carac} caracteres desconsiderando espaços!')