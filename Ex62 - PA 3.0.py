# Exercício 62. Melhore o DESAFIO061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

from time import sleep

termo = [int(input('Digite o primeiro termo da PA: '))]
razao = int(input('Digite a razão da PA: '))
c = 0

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

while c < 10:
    print(f'O {c+1}° termo desta PA é: {termo[c]}')
    termo.append(termo[c] + razao)
    c += 1
print('\033[1;33m=-\033[m' * 60)
d = c
resposta = input('\033[1;31mVocê deseja verificar mais algum termo? (Digite a quantidade de termos a mais ou 0 para encerrar): \033[m').strip()
while not resposta.isnumeric():
    print('\033[1;31mDIGITE UM VALOR NUMÉRICO VÁLIDO!!!\033[m')
    resposta = input('Quantos termos a mais você deseja verificar? (Digite 0 caso não queira): ').strip()
resposta = int(resposta)
while resposta > 0:
    respostac = resposta+d
    while d < respostac:
        print(f'O {d + 1}° termo desta PA é: {termo[d]}')
        termo.append(termo[d] + razao)
        d += 1
    print('\033[1;33m=-\033[m' * 60)
    resposta = input('\033[1;31mVocê deseja verificar mais algum termo? (Digite a quantidade de termos a mais ou 0 para encerrar): \033[m').strip()
    while not resposta.isnumeric():
        print('\033[1;31mDIGITE UM VALOR NUMÉRICO VÁLIDO!!!\033[m')
        resposta = input('Quantos termos a mais você deseja verificar? (Digite 0 caso não queira): ').strip()
    resposta = int(resposta)
if resposta == 0:
    print('\n\033[1;33mENCERRANDO PROGRAMA!!!\033[m')
    sleep(1)
    print('\033[1;33m...\033[m')
    sleep(1)
    print('\033[1;31mPROGRAMA ENCERRADO!!!\033[m')
