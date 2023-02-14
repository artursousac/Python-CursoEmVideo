# Exercício 88. Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

from random import randint
from time import sleep

jogos = []

quantidadejogos = input('Quantos jogos de 6 números da Mega Sena você deseja gerar?: ').strip()

while not quantidadejogos.isnumeric():
    print('\033[1;31mDIGITE QUANTIDADE DE JOGOS VÁLIDO. MAIOR OU IGUAL A 0!\033[m')
    quantidadejogos = input('Quantos jogos de 6 números da Mega Sena você deseja gerar?: ').strip()

quantidadejogos = int(quantidadejogos)

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mJOGOS DA MEGA SENA CRIADOS\033[m')

for c in range(0, quantidadejogos):
    contador = 0
    jogos.append([])
    while contador < 6:
        num = randint(1,60)
        if num not in jogos[c]:
            jogos[c].append(num)
            contador += 1
    jogos[c].sort()
    print(f'Os números criados para o {c+1}° jogo: \033[1;32m{jogos[c]}\033[m')
    sleep(1)

print('\n\033[1;34mBOA SORTE!!!\033[m')
