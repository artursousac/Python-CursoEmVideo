# Exercício 84. Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

dados = []
lista_pessoas = []
pessoas_leves = []
pessoas_pesadas = []
c = 0
maior = 0
menor = float("INF")

while True:
    contador = 0
    dados.append(input('Digite o nome de uma pessoa: ').strip().lower())
    for c in range(0, len(dados[0])):
        if not dados[0].isalpha():
            contador += 1
        if dados[0] == ' ':
            contador -= 1
    while contador != 0:
        contador = 0
        print('\033[1;31mDIGITE O NOME VÁLIDO DE UMA PESSOA!!! SOMENTE LETRAS E ESPAÇOS.\033[m')
        del dados[0]
        dados.append(input('Digite o nome de uma pessoa: ').strip().lower())
        for c in range(0, len(dados[0])):
            if not dados[0].isalpha():
                contador += 1
            if dados[0] == ' ':
                contador -= 1
    dados.append(input('Digite o peso, em kg, desta pessoa: ').strip())
    while not dados[1].isnumeric():
        print('\033[1;31mDIGITE UM PESO VÁLIDO!!!\033[m')
        del dados[1]
        dados.append(input('Digite o peso, em kg, desta pessoa: ').strip())
    dados[1] = float(dados[1])
    if dados[1] >= maior:
        maior = dados[1]
    if dados[1] <= menor:
        menor = dados[1]
    lista_pessoas.append(dados[:])
    dados.clear()
    resposta = input('\033[1;34mVocê deseja digitar o nome e o peso de mais pessoas? (Sim ou Não): \033[m').strip().lower()
    while resposta not in ['sim', 'nao', 's', 'n', 'não']:
        print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA!!!\033[m')
        resposta = input('\033[1;34mVocê deseja digitar o nome e o peso de mais pessoas? (Sim ou Não): \033[m').strip().lower()
    if resposta in ['nao', 'não', 'n']:
        print('\033[1;33m=-\033[m' * 60)
        break
    print('\033[1;33m=-\033[m' * 60)
    c += 1

for c in range(0, len(lista_pessoas)):
    if lista_pessoas[c][1] == maior:
        pessoas_pesadas.append(lista_pessoas[c][0])
    if lista_pessoas[c][1] == menor:
        pessoas_leves.append(lista_pessoas[c][0])

print(f'Foram cadastradas \033[1;32m{c+1} pessoas\033[m.')
for c in range(0, len(pessoas_leves)):
    if c == 0:
        print(f'O menor peso foi de \033[1;32m{menor}\033[m. Segue lista de nome da(s) pessoa(s) mais leves: {pessoas_leves[c].capitalize()}', end='; ')
    else:
        print(pessoas_leves[c].capitalize(), end='; ')
for c in range(0, len(pessoas_pesadas)):
    if c == 0:
        print(f'\nO menor peso foi de \033[1;32m{maior}\033[m. Segue lista de nome da(s) pessoa(s) mais pesadas: {pessoas_pesadas[c].capitalize()}', end='; ')
    else:
        print(pessoas_pesadas[c].capitalize(), end='; ')
