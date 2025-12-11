# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
from playsound import playsound

# Caminho para o arquivo MP3
caminho_mp3 = 'C:/Users/Roger/Desktop/Estudos/python/CursoemVideo/des21b.mp3' # aqui você coloca o caminho do áudio no seu pc


# Reproduz o arquivo MP3
playsound(caminho_mp3)


"""
2° maneira

import pygame

pygame.mixer.init()

pygame.mixer.music.load('des21b.mp3')
pygame.mixer.music.play()

x = input('Digite algo para a música parar...')"""
