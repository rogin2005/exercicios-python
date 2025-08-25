# 9° aula de python aprendendo fatiamento de texto...
# 'Curso em vídeo Python'

frase = 'Curso em Vídeo Python'
frase1 = '   Aprenda Python  '
# Exemplos de Fatiamento de string:

print('-'*20, 'Fatiamento', '-'*20 )
# pega o 9° caractere de frase
print('1° Ex: ', frase[9])
# pega entre o 9° e o 13° caractere de frase
print('2° Ex: ', frase[9:13])
# pega entre o 9° e o 14° caractere de frase
print('3° Ex: ', frase[9:14])
# pega entre o 9° e o 21° caractere de frase
print('4° Ex: ', frase[9:21])
# pega entre o 9° e o 21° caractere de frase, porém com o salto de 2 caracteres
print('5° Ex: ', frase[9:21:2])
# pega do começo de frase "0" e vai até o caractere 5
print('6° Ex: ', frase[:5])
# pega do caractere 15 e vai até o final de frase
print('7° Ex: ', frase[15:])
# pega do caractere 9 e vai até o final da frase, porém com um salto de 3 caracteres
print('8° Ex: ', frase[9::3])
print('-'*53)

# Observações: 1°: no fatiamento o ultimo caractere, que no caso seria o caractere informado ele é ignorado no reultado final. EX: "frase[9:14]" ele só irá mostrar até o caracter 13, ou seja se vc quisesse pegar o 14 também no resultado teria que fazer: "frase[9:15]"

# Exemplos de Análise de string: 

print('-'*20, 'Análise', '-'*20 )
# Me diz o tamanho da frase.
print('Tamanho da frase:', len(frase))
# Me diz quantas letras "o" tem em toda a string.
print('Contagem de letra "o":', frase.count('o'))
# Me diz quantas letras "o" entre 0 e 13, lembrando da 1° obs.
print('Contagem de "o" de 0 a 13:', frase.count('o', 0, 13))
# Indica em qual posição começa o texto q vc colocou entre parênteses.
print('Indicando onde começa o "deo":', frase.find('deo'))
# Vai me retornar -1, pois simplesmente ele verifica que esse texto ñ existe dentro da string.
print('Verificando texto inexistente:', frase.find('Android'))
# Me mostra se existe um texto dentro da string usando o método "in" e retorna um valor booleano.
print('Verifique se existe "Curso" dentro de "frase":', 'Curso' in frase)
print('-'*50)

# Exemplos de Tranformação de string.

print('_'*20, 'Transformação', '_'*20)
# Faz com que a palavra "Python" seja substituída por "Android" dentro de frase.
print(frase.replace('Python', 'Android'))
# Transforma toda a string em caixa alta (Caps Lock).
print(frase.upper())
# Transforma toda a string em minúsculas.
print(frase.lower())
# Tranforma toda a string em minúsculas mas mantem a primeira letra da string maiúscula.
print(frase.capitalize())
# Transoforma toda primeira letra de todas as palavras da string em maiúsculas.
print(frase.title())
# vai remover todos os espaços desnecessários da string do começo e do final.
print(frase1.strip())
# remove somente os espaços desnecessários do lado direito.
print(frase1.rstrip())
# remove somento os espaços desnecessários de lado esquerdo.
print(frase1.lstrip())
print('_'*50)

# Exemplos de divisão de string.

print('_'*20, 'Divisão', '_'*20)
# faz uma enumeração de palavras dividindo elas de acordo com os espaçõs dados, ou seja a cada espaço ela faz um novo index. (uma lista)
print(frase.split())
print('_'*50)

# Exemplo de junção

print('_'*20, 'Junção', '_'*20)
# Adiciona o - entre todas as letras da string.
print('-'.join(frase))
# Adiciona o - no lugar dos espaços da string.
print('-'.join(frase.split()))
print('_'*50)

# Exemplo de print de parágrafo.

print("""Depois de conectado à VPN, seu computador estará na mesma rede que o servidor local, permitindo que você acesse recursos compartilhados, pastas, impressoras e outros serviços como se estivesse fisicamente presente na rede local.""")

# Experimentos:

print('Conte quantos "O" tem:', frase.upper().count('O'))
print(len(frase1.strip()))
print(frase.lower().find('vídeo'))

print('_'*50)
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2] [3])