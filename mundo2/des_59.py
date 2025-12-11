# Crie um programa que leia dois valores e mostre um menu na tela: [1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa / Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

print('''
Olá gafanhoto seja bem vindo ao meu programa de operações!
A seguir vou pedir que vc me informe dois números...
      ''')

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
maior = num_1
opcao = 1


while opcao != 5:
      print('''Menu:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Sua escolha: ''')
      opcao = int(input('Com base no menu decida oq fazer de 1 a 5: '))
      sleep(1)
      if opcao == 1:
            print(f'a soma entre {num_1} e {num_2} é igual a {num_1 + num_2}')
      elif opcao == 2:
            print(f'a multiplicação entre {num_1} e {num_2} é igual a {num_1 * num_2}')
      elif opcao == 3:
            if num_2 > maior:
                  maior = num_2
            print(f'O maior número entre os dois é {maior}')
      elif opcao == 4:
            print('Digite novos números...')
            num_1 = int(input('Digite o novo primeiro valor: '))
            num_2 = int(input('Digite o novo segundo valor: '))
      elif opcao == 5:
            print('Finalizando...')
      else:
            print('Opção inválida. Tente novamente...')
      print('=-='*30)
      sleep(1)
print(f'Tchau até mais...')

#Corrigido, teve alguns ajustes para ficar bom com ajuda do guanabara e ficou muito bom!
