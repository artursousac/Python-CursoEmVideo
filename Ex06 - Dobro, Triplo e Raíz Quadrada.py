# Exercício 06 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = float(input('Digite um número que você deseja descobrir o dobro, triplo e a raíz quadrada: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print(f'O dobro, triplo e a raíz quadrada do {num} é igual, respectivamente, a: {dobro}, {triplo} e {raiz}')
