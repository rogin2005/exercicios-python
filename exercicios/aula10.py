# entendendo condicionais...

#if condição:
#   faça algo se "condição" for verdadeira
#else:
#   faça outra coisa se "condição" for falsa    

# método normal
casa = int(input('Digite quantos banheiros tem em sua casa: '))
if casa <= 5:
    print('Casa pequena')
else:
    print('Casa grande')
    

# método simplificado
vida = int(input('Digite 1 para ter vida ou qualquer outro número para não ter vida: '))
print('Tem vida' if vida == 1 else 'não tem vida')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')
if m >= 7.0:
    print('Sua média está excelente')
elif m > 5  < 6.9:
    print('está de recuperação')
else:
    print('está reprovado')
print('Sua média está excelente' if m >= 7.0 else 'mizerento')