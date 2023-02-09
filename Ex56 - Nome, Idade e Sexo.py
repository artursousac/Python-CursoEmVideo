# Exercício 56. Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# — A média de idade do grupo. - Qual é o nome do homem mais velho. - Quantas mulheres têm menos de 20 anos.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

nome = []
idade = []
sexo = []
contadornome = 0
contadorsexo = 0
somaidade = 0
maior = 0
contadormulher = 0
nomemaior = 0

for c in range(0,4):
    print(f'\033[1;34m{c+1}° PESSOA\033[m')
    nome.append(input(f'Digite o nome de uma pessoa: ').strip())
    for nometeste in range(0, len(nome[c])):
        if not nome[c][nometeste].isalpha():
            contadornome += 1
            if nome[c][nometeste] == ' ':
                contadornome -= 1
    while contadornome > 0:
        print('\033[1;31mDIGITE UM NOME VÁLIDO!!!\033[m')
        del nome[c]
        nome.append(input('Digite o nome de uma pessoa: ').strip())
        contadornome = 0
        for nometeste in range(0, len(nome[c])):
            if not nome[c][nometeste].isalpha():
                contadornome += 1
                if nome[c][nometeste] == ' ':
                    contadornome -= 1
    idade.append(input(f'Digite a idade desta pessoa: ').strip())
    while not idade[c].isnumeric():
        print('\033[1;31mDIGITE UMA IDADE VÁLIDA!!!\033[m')
        del idade[c]
        idade.append(input(f'Digite a idade desta pessoa: ').strip())
    idade[c] = int(idade[c])
    sexo.append(input(f'Digite o sexo desta pessoa (M ou F): ').upper().strip())
    if sexo[c] != 'M' and sexo[c] != 'F':
        contadorsexo += 1
        while contadorsexo > 0:
            print('\033[1;31mDIGITE UM SEXO VÁLIDO!!! SOMENTE A LETRA M OU F.\033[m')
            del sexo[c]
            sexo.append(input(f'Digite o sexo desta pessoa (M ou F): ').upper().strip())
            if sexo[c] != 'M' and sexo[c] != 'F':
                contadorsexo += 1
            else:
                contadorsexo = 0
    print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')
for c in range(0, len(idade)):
    somaidade += idade[c]
    if idade[c] > maior and sexo[c] == 'M':
        maior = idade[c]
        nomemaior = nome[c]
    if idade[c] < 20 and sexo[c] == 'F':
        contadormulher += 1
media = somaidade / len(idade)


print(f'- A média de idade destas pessoas é de {media:.2f} anos.')
if nomemaior == 0:
    print('- Não foi incluído nenhum homem nesta lista.')
elif nomemaior != 0:
    print(f'- O homem mais velho é o {nomemaior}.')
if contadormulher == 0:
    print('- Nenhuma das mulheres incluídas na lista possue menos de 20 anos.')
elif contadormulher == 1:
    print(f'- {contadormulher} Mulher tem menos de 20 anos.')
else:
    print(f'- {contadormulher} Mulheres possuem menos de 20 anos.')
