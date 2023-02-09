# Exercício 68. Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vítorias consecutivas que ele conquistou ao final do jogo.

import random

print('\033[1;31mBEM VINDO AO JOGO DO PAR OU ÍMPAR. O JOGO SÓ SERÁ INTERROMPIDO QUANDO VOCÊ PERDER.\033[m')
quantidade = 0

while True:
    print('\033[1;33m=-\033[m' * 60)
    imparpar = input('Ímpar ou Par?: ').strip().lower()
    if imparpar == 'impar':
        imparpar = 'ímpar'
    while imparpar not in ['ímpar', 'par']:
        print('\033[1;31mPARA O JOGO ACONTECER, DIGITE SOMENTE ÍMPAR OU PAR NESTA ETAPA!!!\033[m')
        imparpar = input('Ímpar ou Par?: ').strip().lower()
    jogador = input('Digite um valor de 0 a 10: ').strip()
    while not jogador.isnumeric() and jogador not in range(0, 11):
        print('\033[1;31mDIGITE UM NÚMERO VÁLIDO!!!\033[m')
        jogador = input('Digite um valor de 0 a 10: ').strip()
    jogador = int(jogador)
    maquina = random.randint(0, 10)
    soma = jogador + maquina
    if soma % 2 == 0:
        resultado = 'par'
    elif soma % 2 != 0:
        resultado = 'ímpar'
    if imparpar == 'ímpar' and resultado == 'ímpar':
        print(f'\033[1;33mPARABÉNS.\033[mVOCÊ GANHOU. O COMPUTADOR ESCOLHEU {maquina}. VAMOS JOGAR NOVAMENTE.')
        quantidade += 1
    elif imparpar == 'ímpar' and resultado == 'par':
        print(f'\033[1;31mQUE PENA.\033[mVOCÊ PERDEU. O COMPUTADOR ESCOLHEU {maquina}.\nVOCÊ GANHOU {quantidade} PARTIDAS')
        break
    elif imparpar == 'par' and resultado == 'par':
        print(f'\033[1;33mPARABÉNS.\033[mVOCÊ GANHOU. O COMPUTADOR ESCOLHEU {maquina}. VAMOS JOGAR NOVAMENTE.')
        quantidade += 1
    elif imparpar == 'par' and resultado == 'ímpar':
        print(f'\033[1;31mQUE PENA.\033[mVOCÊ PERDEU. O COMPUTADOR ESCOLHEU {maquina}.\nVOCÊ GANHOU {quantidade} PARTIDAS')
        break
