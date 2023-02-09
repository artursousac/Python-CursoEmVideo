# Exercício 38. Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem na tela: - O primeiro valor é maior. - O segundo valor é maior.
# - Não existe valor maior, pois os dois são iguais.

print('\033[1;31mENTRADAS DO USUÁRIO\033[0;m')

num1 = float(input('Digite o valor do primeiro número: '))
num2 = float(input('Digite o valor do segundo número: '))

print('\033[1;33m-=\033[0,m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[0;m')

if num1 > num2:
    print(f'O primeiro valor ({num1}) é maior que o segundo valor ({num2}).')
elif num2 > num1:
    print(f'O segundo valor ({num2}) é maior que o primeiro valor ({num1}).')
else:
    print('Não existe valor maior, pois os dois são iguais.')
