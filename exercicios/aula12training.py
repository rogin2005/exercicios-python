nome = str(input('Qual o seu nome? '))

if nome == 'Roger':
    print(f'Que nome lindo vc tem {nome}!!!')
elif nome == 'Francisco' or nome == 'Maria' or nome == 'José':
    print('Seu nome é bem popular em território brasileiro.')
elif nome in 'Victor Hugo Ricardo Léo Júlio':
    print('Belo nome masculino!')
print(f'Seja bem vindo {nome}!')