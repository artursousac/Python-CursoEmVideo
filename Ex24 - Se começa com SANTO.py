# Exercício 24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

nomecidade = input('Digite o nome de uma cidade: ')

santo = 'SANTO' in nomecidade.upper()[0:5]

print(f'Esta cidade começa com o nome "SANTO"?\nR = {santo}')
