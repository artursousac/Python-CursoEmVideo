# Exercício 32. Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite um ano qualquer: '))

if ano % 4 == 0:
    print('\nEste é um ano BISSEXTO!')
else:
    print('\nEste não é um ano BISSEXTO')
