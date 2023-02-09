# Exercício 27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = input('Digite o nome completo de uma pessoa: ')

primeiro = nome[0:nome.find(' ')]
ultimo = nome[nome.rfind(' ')+1:]

print(f'Primeiro nome: {primeiro}\nÚltimo nome: {ultimo}')
