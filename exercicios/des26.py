fra = str(input('Digite uma frase: ')).upper().strip()
print('Quantos A aparece na frase:', fra.count("A"))
print('O primeiro a aparece na posicão:', fra.find('A')+1)
print('O último a aparece na posição:', fra.rfind('A')+1)