# Exercício 92. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá, também, o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. 35 anos de contribuição.

from datetime import date

print('\033[1;31mCÁLCULO DE APOSENTADORIA\033[m')

dadosPessoa = {}

start = 0
contador = 0
anoNascimento = '0'

#NOME
while contador > 0 or start == 0:
    if contador > 0 and start != 0:
        print('\033[1;31mDIGITE O NOME DE UM JOGADOR VÁLIDO\033[m')
    start = 1
    nome = input(f'Digite o nome do usuário que deseja verificar a situação previdenciária: ').strip().lower()
    contador = 0
    for i in range(0, len(nome)):
        if not nome[i].isalpha():
            contador += 1
        if nome[i] == ' ':
            contador -= 1
        if (len(nome.split()) - nome.count(' ')) != 1:
            contador += 1
dadosPessoa['Nome'] = nome.title()
#ANO DE NASCIMENTO
anoNascimento = input('Digite o ano de nascimento: ').strip().lower()
while True:
    while not anoNascimento.isnumeric():
        print('\033[1;31mDIGITE UM ANO DE NASCIMENTO VÁLIDO!!!\033[m')
        anoNascimento = input('Digite o ano de nascimento: ').strip().lower()
    anoNascimento = int(anoNascimento)
    while date.today().year - int(anoNascimento) < 0 or date.today().year - int(anoNascimento) > 130:
        print('\033[1;31mDIGITE UM ANO DE NASCIMENTO VÁLIDO!!!\033[m')
        anoNascimento = input('Digite o ano de nascimento: ').strip().lower()
    if type(anoNascimento) == int and date.today().year - anoNascimento >= 0:
        break
dadosPessoa['Idade'] = date.today().year - anoNascimento
#CARTEIRA DE TRABALHO
carteiraTrabalho = input('Digite o número da CTPS (digite "0" caso não possua): ').strip()
while not carteiraTrabalho.isnumeric():
    print('\033[1;31mDIGITE A NUMERAÇÃO CORRETA DA CTPS. SOMENTE NÚMEROS!!!\033[m')
    carteiraTrabalho = input('Digite o número da CTPS (digite "0" caso não possua): ').strip()
dadosPessoa['CTPS'] = carteiraTrabalho
#ANO CONTRATAÇÃO E SALÁRIO
if dadosPessoa['CTPS'] != '0':
    anoContratacao = input('Digite o ano da contratação: ').strip()
    while not anoContratacao.isnumeric() or date.today().year - int(anoContratacao) < 0:
        print('\033[1;31mDIGITE UM ANO VÁLIDO!!!\033[m')
        anoContratacao = input('Digite o ano da contratação: ').strip()
    salario = input('Digite o salário da CTPS (Em caso de valor quebrado, arredondar para baixo): ').strip()
    while not salario.isnumeric() or float(salario) < 0:
        print('\033[1;31mDIGITE UM SALÁRIO VÁLIDO!!!\033[m')
        salario = input('Digite o salário da CTPS (Em caso de valor quebrado, arredondar para baixo): ').strip()
    salario = float(salario)
    dadosPessoa['Ano de Contratação'] = anoContratacao
    dadosPessoa['Salário'] = salario

idadeAposentadoria = (int(anoContratacao) - anoNascimento) + 35
anoAposentadoria = int(anoContratacao) + 35

print('\033[1;33m=-\033[m' * 60)
print('\033[1;34mDADOS DO USUÁRIO\033[m')
print(f'Nome = {dadosPessoa["Nome"]}\n'
      f'Idade = {dadosPessoa["Idade"]} Anos\n'
      f'CTPS = {dadosPessoa["CTPS"]}\n'
      f'Ano de Contratação = {dadosPessoa["Ano de Contratação"]}\n'
      f'Salário = R$ {dadosPessoa["Salário"]:.2f}\n'
      f'Idade de aposentadoria = Se aposentará com {idadeAposentadoria} Anos em {anoAposentadoria}')

