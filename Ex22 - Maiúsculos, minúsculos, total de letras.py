# Exercício 22 - Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas; O nome com todas minúsculas; Quantas letras ao total sem considerar os espaços;
# Quantas letras tem o primeiro nome;

NomeCompleto = input('Digite o seu nome completo com maiúsculas e minúsculas: ')
print(f'\nO nome completo digitado foi: {NomeCompleto}')

NomeMaiusculo = NomeCompleto.upper()
print(f'\nO nome digitado, com todas as letras maiúsculas, é: {NomeMaiusculo}')

NomeMinusculo = NomeCompleto.lower()
print(f'\nO nome digitado, com todas as letras minúsculas, é: {NomeMinusculo}')

TotalLetras = len(NomeCompleto.strip().replace(' ', ''))
print(f'\nO total de letras, sem considerar os espaços, é: {TotalLetras}')
