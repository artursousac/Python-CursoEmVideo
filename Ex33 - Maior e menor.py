# Exercício 33. Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
numero3 = float(input('Digite outro número: '))

if numero1 > numero2 and numero2 > numero3:
    print(f'\nO número {numero1} é o maior e o número {numero3} é o menor!')
if numero2 > numero1 and numero1 > numero3:
    print(f'\nO número {numero2} é o maior e o número {numero3} é o menor!')
if numero2 > numero3 and numero3 > numero1:
    print(f'\nO número {numero2} é o maior e o número {numero1} é o menor!')
if numero1 > numero3 and numero3 > numero2:
    print(f'\nO número {numero1} é o maior e o número {numero2} é o menor!')
if numero3 > numero1 and numero1 > numero2:
    print(f'\nO número {numero3} é o maior e o número {numero2} é o menor!')
if numero3 > numero2 and numero2 > numero1:
    print(f'\nO número {numero3} é o maior e o número {numero1} é o menor!')
