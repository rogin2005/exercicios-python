msg = "Curso em Vídeo muito massa"
msg2 = "    Oi sou eu de Novo!     "
print(msg.replace('Vídeo', 'Los Angeles'))

if 'Curso' in msg:
    print('Curso existe dentro da nossa mensagem!')
    
# Passando a string inteira para maiúsculo
print(msg.upper())

# Passando a string inteira para minúsculo
print(msg.lower())

# Passando somente a primeira letra da string para maiúscula
print(msg.capitalize())

# Passando todas as primeiras letras de palavras dentro da string para maiúsculas
print(msg.title())

# Tirando espaços em branco antes da primeira palavra e depois da última da string
print(msg2.strip())

# Tirando espaços em branco antes da primeira palavra e depois da última da string
print(len(msg2.strip()))

# Verificando o tamanho da minha string contando espaços e tudo
print(len(msg2))

# rstrip tira todos os espaços do lado direito da string ou depois da última palavra.
print(msg2.rstrip())

# retira todos os espaços do lado esquerdo da string ou antes da primeira palavra.
print(msg2.lstrip())

# split é uma função que separa a string normalmente por espaços entre palavras e gera uma lista com as palavras separadas
f1 = msg.split()

# o join serve para inserir em uma string uma configuração de separação por indexação, por exemplo como eu já tinha minha string dividida na variável anterior então eu peguei minha variável e usei o join com hífen, mas tem vários outros casos que ele pode ser útil.
print('-'.join(f1))

print(msg[1:15])

print(msg[:15])

print(msg[::])

print(msg[1:15:2])

print(msg[::2])

print(""" o join serve para inserir em uma string uma configuração de separação por indexação, por exemplo como eu já tinha minha string dividida na variável anterior então eu peguei minha variável e usei o join com hífen, mas tem vários outros casos que ele pode ser útil. """)

print(msg.count('o'))

print(msg.upper().count('O'))

print(msg.find('Curso'))

print(msg.find('Python'))

print(msg.find('massa'))

print(msg.upper().find('CURSO'))

dividido = msg.split()

print(dividido[2])

print(dividido[2][1])


# Exercício útil...
frase = str(input('Digite uma frase: ')).upper()
print('A(s):', frase.upper().count("A"))
print('posição primeiro A:', frase.upper().find("A"))
print('último A:', frase.rfind("A"))


# if simplificado
analise = int(input('digite sua idade: '))

print('maior de 10 anos'if analise >= 10 else 'menor de 10 anos')
