cid = str(input('Digite aqui a cidade que vc nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')

# 2° maneira:
"""city = str(input('Digite o nome da sua cidade: ')).split()

print('SANTO' in city[0].upper())
print(city[0].upper())"""