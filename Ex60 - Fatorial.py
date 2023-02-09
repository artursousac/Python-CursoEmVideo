# Exercício 60. Faça um programa que leia um número qualquer e mostre seu fatorial.

print('\033[1;31mENTRADA DO USUÁRIO\033[m')

numero = input('Digite um número que você deseja saber seu fatorial: ')
while not numero.isnumeric():
    print('\033[1;31mDIGITE UM NÚMERO VÁLIDO!!!\033[m')
    numero = input('Digite um número que você deseja saber seu fatorial: ')


fatorial = int(numero)
c = int(numero)

while c > 1:
    c -= 1
    fatorial = fatorial * c

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

print(f'O fatorial de {numero} é: {fatorial}')
