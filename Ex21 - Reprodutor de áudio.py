# Exercício 21 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

resposta = input('Digite "musica" se você quiser escutar uma música: ')

if resposta == 'musica':
    pygame.init()  # Este comando serve para iniciar o pygame.
    pygame.mixer.music.load('CompletaFrase.mp3')  # Este comando serve para "chamar" a música, que deve estar na pasta de onde o arquivo deste programa vai estar.
    pygame.mixer.music.play()  # Aqui é para dar play na música.
    input()  # Necessita para o programa rodar com som.
    pygame.event.wait()