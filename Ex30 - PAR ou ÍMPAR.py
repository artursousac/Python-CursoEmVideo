# Exercício 30 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número: '))

if numero % 2 == 0 and numero != 0:
    print('O número digitado é PAR')
if numero == 0:
    print('O número digitado é NEUTRO')
if numero % 2 != 0:
    print('O número digitado é ÍMPAR')
