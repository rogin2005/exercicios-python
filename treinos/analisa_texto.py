# analisar texto - frase
frase = input('Digite uma frase qualquer: ').upper()
frase_s = frase.split()
print(f'a frase contem {len(frase_s)} palavras!')
print(frase)
if 'PYTHON' in frase:
    print('Tem python na frase')
else:
    print('não tem python na frase')