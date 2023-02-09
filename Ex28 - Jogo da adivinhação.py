# Exercício 28 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa
# deverá escrevar na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('-=' * 70)
print('Bem vindo ao jogo da adivinhação, o computador irá escolher um número de 0 a 5 e você irá tentar descobrir qual foi, vamos começar?')
print('-=' * 70)

resposta = 'SIM'

while resposta == 'SIM':

    armazenamento = randint(0, 5)
    numero = int(input('\nDigite um número de 0 a 5: '))
    print('PROCESSANDO...')
    sleep(2)

    if numero == armazenamento:
        print('Parabéns, você adivinhou o número!')
    else:
        print(f'Que pena, você perdeu, o número correto era o {armazenamento}')
    resposta = input('Você deseja continuar jogando? (Sim ou Não): ').upper()

if resposta == 'NÃO' or 'NAO':
    print('\nObrigado por ter jogado!')
