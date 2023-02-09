# Exercício 45. Crie um programa que faça o computador jogar jokenpô (Pedra, Papel e Tesoura) com você.

import random
import time

print('\033[1;31mBEM VINDO AO JOKENPÔ! NESTE JOGO VOCÊ JOGARÁ CONTRA A MÁQUINA E TERÁ TRÊS OPÇÕES: PEDRA, PAPEL OU TESOURA. VAMOS JOGAR?\033[m')

indicador = '1'
escolha= ['Pedra', 'Papel', 'Tesoura']

while indicador == '1':
    print('\033[1;33m=-\033[m' * 60)
    escolhausuario = input('Escolha Pedra, Papel ou Tesoura: ').capitalize()
    escolhamaquina = random.choice(escolha)
    print('PROCESSANDO...')
    time.sleep(1)
    if escolhausuario == escolhamaquina:
        print(f'EMPATE! Você escolheu {escolhausuario} e a máquina escolheu {escolhamaquina}.')
    elif escolhausuario == 'Pedra' and escolhamaquina == 'Papel':
        print(f'\033[1;31mVOCÊ PERDEU!\033[m Você escolheu \033[1;31m{escolhausuario}\033[m e a máquina escolheu \033[1;32m{escolhamaquina}\033[m.')
    elif escolhausuario == 'Papel' and escolhamaquina == 'Pedra':
        print(f'\033[1;32mVOCÊ GANHOU!\033[m Você escolheu \033[1;32m{escolhausuario}\033[m e a máquina escolheu \033[1;31m{escolhamaquina}\033[m.')
    elif escolhausuario == 'Tesoura' and escolhamaquina == 'Pedra':
        print(f'\033[1;31mVOCÊ PERDEU!\033[m Você escolheu \033[1;31m{escolhausuario}\033[m e a máquina escolheu \033[1;32m{escolhamaquina}\033[m.')
    elif escolhausuario == 'Pedra' and escolhamaquina == 'Tesoura':
        print(f'\033[1;32mVOCÊ GANHOU!\033[m Você escolheu \033[1;32m{escolhausuario}\033[m e a máquina escolheu \033[1;31m{escolhamaquina}\033[m.')
    elif escolhausuario == 'Tesoura' and escolhamaquina == 'Papel':
        print(f'\033[1;32mVOCÊ GANHOU!\033[m Você escolheu \033[1;32m{escolhausuario}\033[m e a máquina escolheu \033[1;31m{escolhamaquina}\033[m.')
    elif escolhausuario == 'Papel' and escolhamaquina == 'Tesoura':
        print(f'\033[1;31mVOCÊ PERDEU!\033[m Você escolheu \033[1;31m{escolhausuario}\033[m e a máquina escolheu \033[1;32m{escolhamaquina}\033[m.')
    else:
        print('OPÇÃO INVÁLIDA!!!')
    indicador = input('Você deseja continuar jogando ([1] - Sim || [2] - Não): ')
    if indicador == '2':
        print('\nOBRIGADO POR TER JOGADO!!!')
    elif indicador != '1':
        while indicador != '1' and indicador != '2':
            indicador = input('OPÇÃO INVÁLIDA!\nVocê deseja continuar jogando ([1] - Sim || [2] - Não): ')
            if indicador == '2':
                print('\nOBRIGADO POR TER JOGADO!!!')
