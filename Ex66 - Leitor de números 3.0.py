# Exercício 66. Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)


print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

soma = 0
quantidade = 0

while True:
    numero = input('Digite um número inteiro (999 para parar): ')
    while not numero.isnumeric():
        print('\033[1;31mDIGITE UM NÚMERO INTEIRO VÁLIDO!!!\033[m')
        numero = input('Digite um número inteiro (999 para parar): ')
    numero = int(numero)
    if numero == 999:
        break
    quantidade += 1
    soma += numero

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

print(f'Foram digitados {quantidade} números e a soma entre eles é de {soma}')
