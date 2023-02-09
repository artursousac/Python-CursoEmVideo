# Exercício 79. Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

valores = []
c = 0

while True:
    valor = input('Digite um valor numérico: ').strip()
    while not valor.isnumeric():
        print('\033[1;31mDIGITE UM NÚMERO VÁLIDO MAIOR OU IGUAL A 0!!!\033[m')
        valor = input('Digite um valor numérico: ').strip()
    valor = int(valor)
    if valor in valores:
        print(f'\033[1;34mO valor {valor} já foi digitado anteriormente!!!\033[m')
    elif valor not in valores:
        valores.append(valor)
    resposta = input('\033[1;34mDeseja digitar mais números? (Sim ou Não): \033[m').strip().lower()
    while resposta not in ['sim', 'não', 'nao', 's', 'n']:
        print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA!!!\033[m')
        resposta = input('\033[1;34mDeseja digitar mais números? (Sim ou Não): \033[m').strip().lower()
    if resposta in ['não', 'nao', 'n']:
        break
    c += 1

valores.sort()

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

print(f'Os valores digitados, em ordem crescente, são:', end= ' ')

for c in valores:
    print(f'\033[1;32m{c}...\033[m', end= ' ')
