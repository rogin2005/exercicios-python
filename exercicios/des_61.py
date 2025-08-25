# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

p_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))

cont = 0 

print(f'{p_termo}, ', end='')
while (cont != 9):
    p_termo += razao
    cont += 1
    print(f'{p_termo}, ', end='')
print('...')
print('Acabou!')
    
# corrigido, guanabara usou uma lógica aproximada da minha com pequenas diferenças e deu certo!