# Exercício 87. Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

matriz = [[], [], []]

somapar = 0
somaterceiracoluna = 0
maior = 0

for c in range(0, 3):
    for i in range(0,3):
        matriz[c].append(input(f'Digite o valor da posição [{c+1},{i+1}]: ').strip())
        while not matriz[c][i].isnumeric():
            print('\033[1;31mDIGITE UM VALOR NUMÉRICO CORRETO!!!\033[m')
            matriz[c].append(input(f'Digite o valor da posição [{c+1},{i+1}]: ').strip())
        matriz[c][i] = int(matriz[c][i])
        if matriz[c][i] % 2 == 0:
            somapar += matriz[c][i]
        if i == 2:
            somaterceiracoluna += matriz[c][i]
        if c == 1:
            if matriz[1][i] > maior:
                maior = matriz[1][i]

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')
print('\033[1;34mMATRIZ 3X3\033[m')

for c in range(0,3):
    for i in range(0,3):
        print(f'\033[1;32m[{matriz[c][i]:^5}]', end=' ')
    print('\n')

print('\033[1;33m=-\033[m' * 60)
print('\033[1;34mSOMA DE TODOS OS VALORES PARES\033[m')
print(f'A soma dos valores pares digitados é: \033[1;32m{somapar}\033[m')

print('\033[1;33m=-\033[m' * 60)
print('\033[1;34mSOMA DOS VALORES DA TERCEIRA COLUNA\033[m')
print(f'A soma dos valores da terceira coluna é de: \033[1;32m{somaterceiracoluna}\033[m')

print('\033[1;33m=-\033[m' * 60)
print('\033[1;34mMAIOR VALOR DA SEGUNDA LINHA\033[m')
print(f'O maior valor da segunda linha é de: \033[1;32m{maior}\033[m')
