# Exercício 74. Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números
# gerados e também indique o menor e o maior valor que estão na tupla.

import random

menor = float("INF")
maior = 0

numerotupla = (random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))

for c in range(0, len(numerotupla)):
    print(f'{numerotupla[c]}', end=' ')
    if numerotupla[c] > maior:
        maior = numerotupla[c]
    if numerotupla[c] < menor:
        menor = numerotupla[c]
#Para maior e menor, existe outra opção que seria utilizar a função max(numerotupla) e min(numerotupla)
print(f'\nO maior número desta tupla é \033[1;32m{maior}.\033[m')
print(f'O menor número desta tupla é \033[1;32m{menor}.\033[m')
