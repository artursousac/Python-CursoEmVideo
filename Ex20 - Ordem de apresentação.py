# Exercício 20 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

print('\nEste programa irá definir a ordem de apresentação dos trabalhos!') #Aqui é para identificar a função do programa para o usuário.

import random #Aqui nós importamos a biblioteca random. Vale destacar que, caso queiramos utilizar somente uma função, podemos usar "from (biblioteca) import (módulo)"

aluno1 = input('\nDigite o nome de um aluno: ') #A partir desta parte, estamos solicitando ao usuário para digitar o nome do aluno.
aluno2 = input('Digite o nome de outro aluno: ')
aluno3 = input('Digite o nome de outro aluno: ')
aluno4 = input('Digite o nome de outro aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

print(f'\nA ordem de apresentação dos trabalhos será: {random.sample(alunos, 4)}') #Vale destacar que podiamos utilizar o módulo random.shuffle (alunos), que iria fazer igual. O sample tem a vantagem
#de poder escolher se será montado a sequência com todos os elementos ou com um número limitado de elementos.

# Para esse código utilizei mais um módulo da biblioteca random, onde monta uma sequência aleatória de acordo com os dados que nós informamos.
