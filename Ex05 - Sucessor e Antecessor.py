# Exercício 05 - Faça um programa que leia um número inteiro e mostra na tela o seu sucessor e o seu antecessor #

num = int(input('Digite um número inteiro que você deseja descobrir seu antecessor e seu sucessor: '))
ant = num - 1
suc = num + 1

print(f'O antecessor e o sucessor, respectivamente, do número {num} é: {ant} e {suc}')
