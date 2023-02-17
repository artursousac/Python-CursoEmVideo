# Exercício 91. Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

jogadores = []

for c in range(0, 4):
    start = 0
    contador = 0
    while contador > 0 or start == 0:
        if contador > 0 and start != 0:
            print('\033[1;31mDIGITE O NOME DE UM JOGADOR VÁLIDO\033[m')
        start = 1
        nome = input(f'Digite o nome do {c + 1}° jogador: ').strip().lower()
        for i in range(0, len(nome)):
            if not nome[i].isalpha():
                contador += 1
            if nome[i] == ' ':
                contador -= 1
    jogadores.append({'nome': nome.capitalize(), 'resultadoDado': randint(1,6)})

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESULTADO DOS JOGADORES\033[m')

for c in range(0, len(jogadores)):
    sleep(1)
    print(f'O/A Jogador(a) \033[1;32m{jogadores[c]["nome"]}\033[m tirou \033[1;32m{jogadores[c]["resultadoDado"]}\033[m no dado.')

ranking = sorted(jogadores, key=itemgetter('resultadoDado'), reverse=True)

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31m--RANKING DOS JOGADORES--\033[m')

for c in range(0, len(ranking)):
    sleep(1)
    print(f'    {c+1}° Lugar: \033[1;32m{ranking[c]["nome"]}\033[m com \033[1;32m{ranking[c]["resultadoDado"]}\033[m.')

