# Exercício 16 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

# Para esse problema, creio que podemos utilizar uma conversão de float para int.

numero = float(input('Digite um número qualquer: '))
numero = int(numero)

print(f'\nO número inteiro do valor digitado é: {numero}')

'''Outra forma de fazer este desafio seria utilizando o módulo trunc da biblioteca math.

from math import trunc #Desse modo, só importamos um módulo em vez de toda a biblioteca.

numero = float(input('\nDigite um número qualquer: '))

print(f'\nO número digitado foi o {numero} e seu valor inteiro é {trunc(numero)}')'''
