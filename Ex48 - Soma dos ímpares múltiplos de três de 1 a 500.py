# Exercício 48. Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('\033[1;31mNÚMEROS ÍMPARES MÚLTIPLOS DE TRÊS ENTRE 1 E 500\033[m')

soma = 0
total = 0

for c in range(1,501):
  if c%2 != 0 and c%3 == 0:
    soma += c
    total += 1

print(f'\nO valor da soma entre todos os {total} números ímpares que são múltiplos de três e que se encontram de 1 até 500 é {soma}')
