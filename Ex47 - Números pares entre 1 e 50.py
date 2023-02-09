# Exercício 47. Crie um programa que mostre na tela todos os números pares no intervalo entre 1 e 50.

i = 0
par = []

for contador in range(1, 51):
    if contador%2 == 0:
        par.append(contador)
        i += 1
print(f'\nOs números pares entre 1 e 50 são: {par}')

"""
Outra forma de fazer esse exercício é usando for contador in range(2, 51, 2). Pois assim ele irá de 2 em 2.
"""