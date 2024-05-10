# Exercício 94. Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas. B) A média de idade do grupo.
# C) Uma lista com todas as mulheres. D) Uma lista com todas as pessoas com idade acima da média.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

# Dicionário para guardar os registros de cada pessoa.
Pessoas = []
contador = 0
start = 0

while True:
    Pessoa = {}
    # Loop para verificar se quer continuar adicionando pessoas na base de dados
    resposta = input('Deseja adicionar uma pessoa na base de dados? (Sim ou Não): ').strip().lower()
    while resposta not in ['sim', 's', 'nao', 'não', 'n']:
        print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA!!! SIM OU NÃO.\033[m')
        resposta = input('Deseja adicionar uma pessoa na base de dados? (Sim ou Não): ').strip().lower()
    if resposta in ['sim', 's']:
        # Nome da Pessoa
        while contador > 0 or start == 0:
            if contador > 0 and start != 0:
                print('\033[1;31mDIGITE UM NOME VÁLIDO (CUIDADO COM ESPAÇOS DOBRADOS E SÍMBOLOS)\033[m')
            start = 1
            nome = input('Digite o nome da pessoa: ').strip().title()
            contador = 0
            for i in range(0, len(nome)):
                if not nome[i].isalpha():
                    contador += 1
                if nome[i] == ' ':
                    contador -= 1
                if (len(nome.split()) - nome.count(' ')) != 1:
                    contador += 1
        Pessoa['Nome'] = nome
        start = 0

        # Sexo da Pessoa
        sexo = input('Digite o sexo (M/F): ').strip().lower()
        while sexo not in ['masculino', 'feminino', 'm', 'f']:
            print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA!!! MASCULINO OU FEMININO.\033[m')
            sexo = input('Digite o sexo (M/F): ').strip().lower()
        Pessoa['Sexo'] = sexo

        # Idade
        idade = input('Digite a idade: ').strip().lower()
        while True:
            while not idade.isnumeric():
                print('\033[1;31mDIGITE UMA IDADE VÁLIDA!!!\033[m')
                idade = input('Digite a idade: ').strip().lower()
            idade = float(idade)
            if type(idade) == float:
                break
        Pessoa['Idade'] = idade
        Pessoas.append(Pessoa)

    elif resposta in ['nao', 'n', 'não']:
        print('\033[1;33m=-\033[m' * 60)
        print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')
        quantidadeDePessoasCadastras = len(Pessoas)
        somaIdade = sum(Pessoa['Idade'] for Pessoa in Pessoas)
        mediaIdade = somaIdade / quantidadeDePessoasCadastras
        listaMulheres = [Pessoa['Nome'] for Pessoa in Pessoas if Pessoa['Sexo'] == 'f' or Pessoa['Sexo'] == 'feminino']
        listaAcimaMedia = [Pessoa['Nome'] for Pessoa in Pessoas if Pessoa['Idade'] > mediaIdade]
        print(f'Quantidade de Pessoas Cadastradas: {quantidadeDePessoasCadastras}')
        print(f'Média de Idade: {mediaIdade:.2f}')
        print(f'Lista de Mulheres: {listaMulheres}')
        print(f'Lista de Pessoas Acima da Média de Idade: {listaAcimaMedia}')
        break
