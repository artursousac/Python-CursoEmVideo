# Exercício 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# Para esse problema, podemos utilizar um módulo da biblioteca math, que irá nos retornar o valor da hipotenusa se inserirmos o cateto oposto e o cateto adjacente.

import math

print('\nEste programa servirá somente para triângulos retângulos onde você possua o valor do cateto oposto e do cateto adjacente!')

cateto_oposto = float(input('\nDigite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f'\nO valor da hipotenusa deste triângulo retângulo é de: {hipotenusa}')
