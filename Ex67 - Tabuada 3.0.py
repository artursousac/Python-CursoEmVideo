# Exercício 67. Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
# O programa será interrompido quando o número solicitado for negativo.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

num = 0

while num >= 0:
    num = input('\033[1;33mDigite um número que você deseja saber a tabuada (negativo caso deseje encerrar o programa): \033[m').strip()
    if num[0] == '-':
        print('\033[1;31mENCERRANDO O PROGRAMA.\033[m')
        break
    while not num.isnumeric():
        print('\033[1;31mDIGITE UM NÚMERO VÁLIDO MAIOR OU IGUAL A 0!!!\033[m')
        num = input('\033[1;33mDigite um número que você deseja saber a tabuada (negativo caso deseje encerrar o programa): \033[m').strip()
        if num[0] == '-':
            break
    if num[0] == '-':
        print('\033[1;31mENCERRANDO O PROGRAMA.\033[m')
    else:
        num = int(num)
        print('\033[1;33m=-\033[m' * 60)
        print(f'\033[1;31mTABUADA DO NÚMERO {num}\033[m')
        for c in range(1, 11):
            print(f'{num} x {c} = {num * c}')
