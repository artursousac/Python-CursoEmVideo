# Exercício 69. Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) Quantos
# homens foram cadastrados. C) Quantas mulheres tem menos de 20 anos.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

nome = []
idade = []
sexo = []
c = 0
maior18 = 0
menor20 = 0
masculino = 0
pessoa18 = []
pessoa20 = []
pessoamasc = []

while True:
    print(f'\033[1;34m{c+1}° USUÁRIO\033[m')
    nome.append(input(f'Digite o nome do {c+1}° usuário: ').lower().strip())
    contador = 0
    for i in range(0, len(nome[c])):
        if not nome[c][i].isalpha():
            contador += 1
        if nome[c][i] == ' ':
            contador -= 1
    while contador != 0:
        contador = 0
        print('\033[1;31mDIGITE UM NOME VÁLIDO!!!\033[m')
        del nome[c]
        nome.append(input(f'Digite o nome do {c+1}° usuário: ').lower().strip())
        for i in range(0, len(nome[c])):
            if not nome[c][i].isalpha():
                contador += 1
            if nome[c][i] == ' ':
                contador -= 1
    idade.append(input(f'Digite a idade do {c+1}º usuário: ').strip())
    while not idade[c].isnumeric():
        print('\033[1;31mDIGITE UM VALOR VÁLIDO PARA IDADE!!!\033[m')
        del idade[c]
        idade.append(input(f'Digite a idade do {c+1}º usuário: ').strip())
    idade[c] = int(idade[c])
    if idade[c] > 18:
        maior18 += 1
        pessoa18.append(nome[c])
    sexo.append(input(f'Digite o sexo do {c+1}º usuário (Masculino ou Feminino): ').strip().lower())
    while sexo[c] not in ['masculino', 'feminino']:
        print('\033[1;31mDIGITE UM VALOR VÁLIDO PARA O SEXO. MASCULINO OU FEMININO!!!\033[m')
        del sexo[c]
        sexo.append(input(f'Digite o sexo do {c+1}º usuário (masculino ou feminino): ').strip().lower())
    if sexo[c] == 'feminino' and idade[c] < 20:
        menor20 += 1
        pessoa20.append(nome[c])
    elif sexo[c] == 'masculino':
        masculino += 1
        pessoamasc.append(nome[c])
    print('\033[1;33m=-\033[m' * 60)
    resposta = input('\033[1;32mDeseja adicionar mais usuários? (Sim ou Não): \033[m').strip().lower()
    while resposta not in ['sim', 'não', 'nao']:
        print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA. SIM OU NÃO!!!\033[m')
        resposta = input('Deseja adicionar mais usuários? (Sim ou Não): ').strip().lower()
    print('\033[1;33m=-\033[m' * 60)
    if resposta in ['não', 'nao']:
        break
    c += 1

print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

if maior18 == 0:
    print('Nenhuma pessoa acima de 18 anos foi cadastrada.')
elif maior18 == 1:
    print(f'{maior18} Pessoa acima de 18 anos foi cadastrada. {pessoa18}')
elif maior18 > 1:
    print(f'{maior18} Pessoas acima de 18 anos foram cadastradas. {pessoa18}')
if masculino == 0:
    print('Nenhuma pessoa do sexo masculino foi cadastrada.')
elif masculino == 1:
    print(f'{masculino} Pessoa do sexo masculino foi cadastrada. {pessoamasc}')
elif masculino > 1:
    print(f'{masculino} Homens foram cadastrados. {pessoamasc}')
if menor20 == 0:
    print('Nenhuma mulher com menos de 20 anos foi cadastrada.')
elif menor20 == 1:
    print(f'{menor20} Mulher com menos de 20 anos foi cadastrada. {pessoa20}')
elif menor20 > 1:
    print(f'{menor20} Mulheres com menos de 20 anos foram cadastradas. {pessoa20}')
