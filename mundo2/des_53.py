#crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).upper()
frase = frase.replace(' ', '')

fra_v = frase[::-1]
print(f'Inverso da frase: {fra_v}')

if frase == fra_v:
    print('é palindromo!')
else:
    print('não é palindromo!')


# metodo guanabara com for
"""frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')"""