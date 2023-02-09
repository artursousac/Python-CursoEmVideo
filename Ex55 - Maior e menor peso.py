# Exercício 55. Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

peso = []
maior = 0.0
menor = float("inf")
for c in range(0,5):
    peso.append(input('Digite o peso de uma pessoa: '))
    if not peso[c].isnumeric():
        while not peso[c].isnumeric():
            print('\033[1;31mDIGITE UM PESO VÁLIDO!!!\033[m')
            del peso[c]
            peso.append(input('Digite o peso de uma pessoa: '))
    if peso[c].isnumeric():
        peso[c] = float(peso[c])
        while peso[c] < 0:
            if peso[c] < 0:
                print('\033[1;31mDIGITE UM PESO VÁLIDO!!!\033[m')
                del peso[c]
                peso.append(input('Digite o peso de uma pessoa: '))
                if not peso[c].isnumeric():
                    while not peso[c].isnumeric():
                        print('\033[1;31mDIGITE UM PESO VÁLIDO!!!\033[m')
                        del peso[c]
                        peso.append(input('Digite o peso de uma pessoa: '))
                if peso[c].isnumeric():
                    peso[c] = float(peso[c])
        for cont in range(0, c+1):
            if peso[cont] > maior:
                maior = peso[cont]
            if peso[cont] < menor:
                menor = peso[cont]
print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')
print(f'O maior peso é \033[1;32m{maior}kg\033[m e o menor peso é \033[1;31m{menor}kg\033[m')
