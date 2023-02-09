# Exercício 71. Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
# será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.

from time import sleep

print('\033[1;31mCAIXA ELETRÔNICO\033[m')

contador50 = 0
contador20 = 0
contador10 = 0
contador1 = 0

while True:
    saque = input('Digite o valor a ser sacado (número inteiro): R$ ')
    while not saque.isnumeric():
        print('\033[1;31mDIGITE UM VALOR VÁLIDO A SER SACADO, SOMENTE NÚMERO INTEIRO!!!\033[m')
        saque = input('Digite o valor a ser sacado (número inteiro: R$ ')
    saque = int(saque)
    saqueinicial = saque
    while saque >= 50:
        saque -= 50
        contador50 += 1
    while saque >= 20:
        saque -= 20
        contador20 += 1
    while saque >= 10:
        saque -= 10
        contador10 += 1
    while saque >= 1:
        saque -= 1
        contador1 += 1

    print('\033[1;33m=-\033[m' * 60)
    print('\033[1;34mRETIRADA DO CAIXA\033[m')
    print(f'Para o saque de \033[1;32mR$ {saqueinicial}\033[m você receberá \033[1;32m{contador50} cédulas de R$ 50.00\033[m, \033[1;32m{contador20} cédulas de R$ 20.00\033[m, \033[1;32m{contador10} cédulas de R$ 10.00\033[m e \033[1;32m{contador1} moedas de R$ 1.00.\033[m')
    print('\033[1;33m=-\033[m' * 60)
    resposta = input('Você deseja sacar mais alguma quantia? (Sim ou Não): ')
    while resposta not in ['sim', 'nao', 'não']:
        print('\033[1;31mDIGITE SOMENTE SIM OU NÃO!!!\033[m')
        resposta = input('\033[1;32mVocê deseja sacar mais alguma quantia? (Sim ou Não): \033[m')
    if resposta in ['nao', 'não']:
        print('\033[1;31mSAINDO DO CAIXA ELETRÔNICO\033[m')
        sleep(1)
        print('\033[1;33m...\033[m')
        sleep(1)
        print('\033[1;31mSAÍDA REALIZADA COM SUCESSO\033[m')
        break
