# Exercício 51. Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

termo = [int(input('Digite o primeiro termo da PA: '))]
razao = int(input('Digite a razão da PA: '))

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

for c in range(1,10):
    termo.append(termo[c-1] + razao)

print(f'Os 10 primeiros termos desta PA são: {termo}')
