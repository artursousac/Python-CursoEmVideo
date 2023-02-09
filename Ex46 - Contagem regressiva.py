# Exercício 46. Faça um programa que mostre uma contagem regressiva na tela para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
from emoji import emojize

print('\033[1;31mCONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFÍCIO\033[m')

for contador in range(10,0,-1):
    print(f'{contador}')
    sleep(1)

print(emojize(':fireworks::fireworks::fireworks::fireworks:'))
