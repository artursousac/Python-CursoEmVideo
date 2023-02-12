# Exercício 85. Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

valores = [[], []]

for c in range (0, 7):
    valor = input('Digite um valor númerico maior ou igual a 0: ').strip().lower()
    while not valor.isnumeric():
        print('\033[1;31mDIGITE UM NÚMERO MAIOR OU IGUAL A 0 VÁLIDO!!!\033[m')
        valor = input('Digite um valor númerico maior ou igual a 0: ').strip().lower()
    valor = int(valor)
    if valor % 2 == 0:
        valores[0].append(valor)
    elif valor % 2 != 0:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')
print(f'Os valores pares são: \033[1;32m{valores[0]}\033[m\nOs valores ímpares são: \033[1;32m{valores[1]}\033[m')
