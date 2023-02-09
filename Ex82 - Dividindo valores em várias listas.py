# Exercício 82. Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

c = 0
valores = []
valorespar = []
valoresimpar = []


while True:
    print('\033[1;33m=-\033[m' * 60)
    valores.append(input('Digite um número inteiro maior ou igual a 0: ').strip())
    while not valores[c].isnumeric():
        print('\033[1;31mDIGITE UM NÚMERO VÁLIDO MAIOR OU IGUAL A 0!!!\033[m')
        del valores[c]
        valores.append(input('Digite um número inteiro maior ou igual a 0: ').strip())
    valores[c] = int(valores[c])
    if valores[c] % 2 == 0:
        valorespar.append(valores[c])
    elif valores[c] %2 != 0:
        valoresimpar.append(valores[c])
    resposta = input('\033[1;34mVocê deseja digitar mais números? (Sim ou Não): \033[m').strip().lower()
    while resposta not in ['sim', 's', 'nao', 'não', 'n']:
        print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA. SOMENTE SIM OU NÃO!!!\033[m')
        resposta = input('\033[1;34mVocê deseja digitar mais números? (Sim ou Não): \033[m').strip().lower()
    if resposta in ['nao', 'n', 'não']:
        print('\033[1;33m=-\033[m' * 60)
        break
    c += 1

print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')


print(f'As três listas geradas são:\nLista com todos os valores em ordem crescente: \033[1;32m{sorted(valores)}\033[m'
      f'\nLista com os valores \033[1;32mpar\033[m em ordem crescente: \033[1;32m{sorted(valorespar)}\033[m'
      f'\nLista com os valores \033[1;32mímpar\033[m em ordem crescente: \033[1;32m{sorted(valoresimpar)}\033[m')
