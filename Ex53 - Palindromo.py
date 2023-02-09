# Exercício 53. Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

print('\033[1;31mENTRADA DO USUÁRIO\033[m')

frase = str(input('Digite uma frase: ')).strip().lower()
frase = frase.replace(' ', '')
aux = 0

for c in range(0, ((len(frase) - 1) // 2)):
    if frase[c] == frase[len(frase) - (c + 1)]:
        aux = aux + 1
if aux == len(frase) // 2:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')
