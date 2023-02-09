# Exercício 19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que o ajude, lendo o nome deles e escrevendo o nome do escolhido

import random

print('\nEste programa servirá para ajudar um professor a sortear quatro alunos para apagar o quatro!')

aluno1 = input('\nDigite o nome de um aluno: ')
aluno2 = input('Digite o nome do outro aluno: ')
aluno3 = input('Digite o nome do outro aluno: ')
aluno4 = input('Digite o nome do outro aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4] #Criei uma lista para organizar as variáveis e simplificar o código.

print(f'\nO aluno escolhido para apagar o quadro foi o (a) {random.choice(alunos)}')

# A lógica para resolver este problema foi utilizar um módulo da biblioteca random, que sorteia elementos.
