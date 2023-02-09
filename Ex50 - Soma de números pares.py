# Exercício 50. Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

soma = 0

for c in range(0, 6):
    numero = int(input('Digite um número inteiro: '))
    if numero%2 == 0:
        soma += numero

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')
print(f'O valor da soma dos números pares digitados é: {soma}')
