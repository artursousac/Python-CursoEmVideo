# Exercício 86. Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

matriz = [[], [], []]

for c in range(0, 3):
    for i in range(0,3):
        matriz[c].append(input(f'Digite o valor da posição [{c+1},{i+1}]: ').strip())
        while not matriz[c][i].isnumeric():
            print('\033[1;31mDIGITE UM VALOR NUMÉRICO CORRETO!!!\033[m')
            matriz[c].append(input(f'Digite o valor da posição [{c+1},{i+1}]: ').strip())
        matriz[c][i] = int(matriz[c][i])

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

for c in range(0,3):
    for i in range(0,3):
        print(f'\033[1;32m[{matriz[c][i]:^5}]', end=' ')
    print('\n')
