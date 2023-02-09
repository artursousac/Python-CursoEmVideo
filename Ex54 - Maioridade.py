# Exercício 54. Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade (21 anos) e quantas já são maiores.

from datetime import date

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

anonasc = []
menoridade = 0
maioridade = 0
idade = []
ano = date.today().year

for c in range(0,7):
    anonasc.append(input('Digite o ano de nascimento de uma pessoa: '))
    while not anonasc[c].isnumeric():
        print('\033[1;31mDIGITE UM ANO DE NASCIMENTO VÁLIDO!!!\033[m')
        del anonasc[c]
        anonasc.append(input('Digite o ano de nascimento de uma pessoa: '))
    if anonasc[c].isnumeric():
        anonasc[c] = int(anonasc[c])
        while (ano - anonasc[c]) < 0:
            print('\033[1;31mDIGITE UM ANO DE NASCIMENTO VÁLIDO!!!\033[m')
            del anonasc[c]
            anonasc.append(input('Digite o ano de nascimento de uma pessoa: '))
            while not anonasc[c].isnumeric():
                print('\033[1;31mDIGITE UM ANO DE NASCIMENTO VÁLIDO!!!\033[m')
                del anonasc[c]
                anonasc.append(input('Digite o ano de nascimento de uma pessoa: '))
            if anonasc[c].isnumeric():
                anonasc[c] = int(anonasc[c])
        if (ano - anonasc[c]) >= 0:
            idade.append((ano - anonasc[c]))
            if idade[c] < 21:
                menoridade += 1
            else:
                maioridade += 1

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')
print(f'De acordo com as informações digitadas {anonasc} {maioridade} pessoas atingiram a maioridade e {menoridade} pessoas ainda não completaram 21 anos!')
