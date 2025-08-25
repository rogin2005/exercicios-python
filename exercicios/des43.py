# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 
"""
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura * altura)
print(f'Seu imc: {imc:.2f}')

if imc <= 18.4:
    print('Abaixo do peso!')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso ideal!')
elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso!')
elif imc >=30 and imc <= 39.9:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')

# concluído...
