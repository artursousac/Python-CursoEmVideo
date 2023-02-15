# Exercício 89. Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

lista_alunos_notas = []
c = -1
media = []
aux = 0
from time import sleep

while True:
    c += 1
    lista_alunos_notas.append([])
    media.append([])
    contador = 0
    print(f'\033[1;34m{c + 1}° ALUNO\033[m')
    nome = str(input(f'Digite o nome completo do {c + 1}° aluno: ').strip().lower())
    for o in range(0, len(nome)):
        if not nome[o].isalpha():
            contador += 1
        if nome[o] == ' ':
            contador -= 1
    while contador > 0:
        contador = 0
        print('\033[1;31mDIGITE UM NOME VÁLIDO. SOMENTE LETRAS!!!\033[m')
        nome = str(input(f'Digite o nome completo do {c + 1}° aluno: ').strip().lower())
        o = 0
        for o in range(0, len(nome)):
            if not nome[o].isalpha():
                contador += 1
            if nome[o] == ' ':
                contador -= 1
    lista_alunos_notas[c].append(nome)
    nota1 = input(f'Digite a primeira nota do {c + 1}° aluno: ').strip()
    contador = 0
    for p in range(0, len(nota1)):
        if not nota1[p].isnumeric():
            contador += 1
        if nota1[p] == ' ' or nota1[p] == '':
            contador += 1
        if nota1[p] == '.':
            contador -= 1
    while contador > 0:
        contador = 0
        print('\033[1;31mDIGITE UMA NOTA VÁLIDA MAIOR OU IGUAL A 0 E MENOR OU IGUAL A 10!!!\033[m')
        nota1 = input(f'Digite a primeira nota do {c + 1}° aluno: ').strip()
        p = 0
        for p in range(0, len(nota1)):
            if not nota1[p].isnumeric():
                contador += 1
            if nota1[p] == ' ' or nota1[p] == '':
                contador += 1
            if nota1[p] == '.':
                contador -= 1
    nota1 = float(nota1)
    lista_alunos_notas[c].append(nota1)
    nota2 = input(f'Digite a segunda nota do {c + 1}° aluno: ').strip()
    contador = 0
    p = 0
    for p in range(0, len(nota2)):
        if not nota2[p].isnumeric():
            contador += 1
        if nota2[p] == ' ' or nota2[p] == '':
            contador += 1
        if nota2[p] == '.':
            contador -= 1
    while contador > 0:
        contador = 0
        print('\033[1;31mDIGITE UMA NOTA VÁLIDA MAIOR OU IGUAL A 0 E MENOR OU IGUAL A 10!!!\033[m')
        nota2 = input(f'Digite a segunda nota do {c + 1}° aluno: ').strip()
        p = 0
        for p in range(0, len(nota2)):
            if not nota2[p].isnumeric():
                contador += 1
            if nota2[p] == ' ' or nota2[p] == '':
                contador += 1
            if nota2[p] == '.':
                contador -= 1
    nota2 = float(nota2)
    lista_alunos_notas[c].append(nota2)
    media[c].append((nota1 + nota2)/2)
    resposta = input('Deseja digitar os dados de outro aluno? (Sim ou Não): ').strip().lower()
    while resposta not in ['sim', 's', 'nao', 'não', 'n']:
        print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA!!! SIM OU NÃO.\033[m')
        resposta = input('Deseja digitar os dados de outro aluno? (Sim ou Não): ').strip().lower()
    if resposta in ['nao', 'n', 'não']:
        break
print('\033[1;33m=-\033[m' * 60)
sleep(1)
print('\033[1;34mBOLETIM ESCOLAR COM MÉDIA DOS ALUNOS\033[m')
sleep(1)
print(f'{"N°":<4}{"NOME DO ALUNO":<25}{"MÉDIA"}')
print('-'*50)
c = 0
for c in range(0, len(lista_alunos_notas)):
    sleep(1)
    print(f'{c+1:<4}{lista_alunos_notas[c][0].capitalize():<25}{media[c][0]:.1f}')
    sleep(1)

while True:
    print('\033[1;33m=-\033[m' * 60)
    resposta = input('Deseja verificar as notas de algum aluno específico? (Sim ou Não): ').strip().lower()
    while resposta not in ['sim', 's', 'nao', 'não', 'n']:
        print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA!!! SIM OU NÃO.\033[m')
        resposta = input('Deseja verificar as notas de algum aluno específico? (Sim ou Não): ').strip().lower()
    if resposta in ['nao', 'n', 'não']:
        print('\033[1;31mOBRIGADO POR TER UTILIZADO ESTE PROGRAMA!!!\033[m')
        break
    while aux == 0:
        resposta = input('Digite o mesmo nome cadastrado do aluno que você deseja verificar a nota: ').strip().lower()
        c = 0
        for c in range(0, len(lista_alunos_notas)):
            if resposta in [lista_alunos_notas[c][0]]:
                sleep(1.5)
                print(f'A nota 1 e nota 2, respectivamente, do(a) {lista_alunos_notas[c][0].capitalize()} foi: '
                  f'\033[1;32m{lista_alunos_notas[c][1]}\033[m e \033[1;32m{lista_alunos_notas[c][2]}\033[m')
                sleep(1.5)
                aux += 1
        if aux == 0:
            print('\033[1;31mESTE ALUNO NÃO FOI CADASTRADO. TENTE NOVAMENTE!!!\033[m')
