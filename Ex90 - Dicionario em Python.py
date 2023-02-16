# Exercício 90. Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

alunos = []
c = 0
situacao = 'EM ANÁLISE'
from time import sleep

while True:
    contador = 0
    nome = input(f'Digite o nome do {c+1}° aluno: ').strip().lower()
    for i in range(0, len(nome)):
        if not nome[i].isalpha():
            contador += 1
        if nome[i] == ' ':
            contador -= 1
    while contador > 0:
        print('\033[1;31mDIGITE UM NOME VÁLIDO!!!\033[m')
        contador = 0
        nome = input(f'Digite o nome do {c + 1}° aluno: ').strip().lower()
        i = 0
        for i in range(0, len(nome)):
            if not nome[i].isalpha():
                contador += 1
            if nome[i] == ' ':
                contador -= 1
    media = input(f'Digite a média de {nome.capitalize()}: ').strip()

    i = 0
    contador = 0

    for i in range(0, len(media)):
        if not media[i].isnumeric():
            contador += 1
        if i == 1:
            if media[i]:
                contador -= 1
    if contador == 0:
        media = float(media)
    while contador > 0 or media > 10:
        contador = 0
        print('\033[1;31mDIGITE UMA MÉDIA VÁLIDA!!! MAIOR OU IGUAL A 0 E MENOR OU IGUAL A 10\033[m')
        media = input(f'Digite a média de {nome.capitalize()}: ').strip()
        i = 0
        for i in range(0, len(media)):
            if not media[i].isnumeric():
                contador += 1
            if i == 1:
                if media[i]:
                    contador -= 1
        if contador == 0:
            media = float(media)
    media = float(media)

    if media >= 7:
        situacao = '\033[1;32mAPROVADO\033[m'
    elif media < 7:
        situacao = '\033[1;31mREPROVADO\033[m'

    alunos.append({'nome': nome.capitalize(), 'média': media, 'situação': situacao})

    print('\033[1;33m=-\033[m' * 60)

    resposta = input('\033[1;34mDeseja adicionar mais um aluno? (Sim ou Não): \033[m').strip().lower()

    while resposta not in ['sim', 's', 'não', 'nao', 'n']:
        print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA!!! SOMENTE SIM OU NÃO.\033[m')
        resposta = input('\033[1;34mDeseja adicionar mais um aluno? (Sim ou Não): \033[m').strip().lower()

    print('\033[1;33m=-\033[m' * 60)

    if resposta in ['não', 'nao', 'n']:
        break

    c += 1

print('\033[1;31mLISTA DE ALUNOS\n\033[m')

c = 0
for c in range(0, len(alunos)):
    sleep(1)
    print(f'{c+1}° Aluno: {alunos[c]["nome"]}\n'
          f'Média: {alunos[c]["média"]}\n'
          f'Situação: {alunos[c]["situação"]}')
    sleep(1)
    print('\033[1;33m=-\033[m' * 60)

