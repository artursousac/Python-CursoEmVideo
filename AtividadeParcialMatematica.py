"""
Nome: Artur Cavalcante de Sousa
Matrícula: 2313541
Disciplina: Matemática para Computação
Atividade Parcial 1
- - - - - - - - - - - - - - - - - - - - - - - - - - - -
Neste momento, sua equipe acaba de ser contratada
pelo Governo Federal, mais especificamente pela Caixa
Econômica Federal (órgão que administra o sorteio da
Mega-Sena), para compor um time de cientistas da
computação responsável por elaborar um código de
programação voltado para os sorteios dos números
premiados.

Esse código deverá gerar aleatoriamente 6 números, de
um total de 60 dezenas (de 01 a 60). Utilize para tanto as
técnicas disponíveis na literatura e desenvolva um código
de programação. Poderá ser utilizada qualquer
linguagem de programação e também o Excel.
"""
print('\033[1;33m=-\033[m' * 16)
print(f'\033[1;34m{"MEGA-SENA":^27}\033[m')
print('\033[1;33m=-\033[m' * 16)

from random import randint
from time import sleep

jogos = [[]]

contador = 0
while contador < 6:
    num = randint(1,60)
    if num not in jogos[0]:
        jogos[0].append(num)
        contador += 1

for c, v in enumerate(jogos[0]):
    print(f'O {c+1}° número sorteado foi: \033[1;32m{v}\033[m')
    sleep(1)

print('\033[1;33m=-\033[m' * 60)
sleep(1)
jogos[0].sort()

print(f'Os números sorteados, em ordem, do menor para o maior, para o próximo sorteio da Mega-Sena são: \033[1;32m{jogos[0]}\033[m')
