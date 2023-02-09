# Exercício 52. Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

numero = int(input('Digite um número: '))
contador = 0

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

for c in range(1, numero+1):
    if numero%c == 0:
        contador += 1
    if contador == 3:
        break

if contador <= 2:
    print(f'O número {numero} é um número primo!')
else:
    print(f'O número {numero} \033[1;31mNÃO\033[m é um número primo!')
