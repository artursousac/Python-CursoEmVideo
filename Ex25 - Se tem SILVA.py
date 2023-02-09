# Exercício 25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite o seu nome completo: ')

silva = 'SILVA' in nome.upper()

print(f'Seu nome contém a palavra "SILVA"?:\nR = {silva}')
