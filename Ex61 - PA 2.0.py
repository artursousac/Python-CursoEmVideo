# Exercício 61. Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

termo = [int(input('Digite o primeiro termo da PA: '))]
razao = int(input('Digite a razão da PA: '))
c = 0

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

while c < 10:
    print(f'O {c+1}° termo desta PA é: {termo[c]}')
    termo.append(termo[c] + razao)
    c += 1
