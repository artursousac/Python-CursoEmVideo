# Exercício 18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Do mesmo modo que os últimos exercícios, podemos utilizar a biblioteca math para nos auxiliar.

import math

anguloGraus = float(input('\nDigite o valor do ângulo, em graus, que você deseja saber o seno, o cosseno e a tangente: '))
anguloRad = math.radians(anguloGraus)
seno = math.sin(anguloRad)
cosseno = math.cos(anguloRad)
tangente = math.tan(anguloRad)

print(f'\nO valor do seno, do cosseno e da tangente é de, respectivamente: {seno:.2f}, {cosseno:.2f}, {tangente:.2f}')

# Para resolver isto, apliquei a conversão de graus para radianos, pois as funções da biblioteca math utilizam o valor em radianos. Após isso, utilizei os módulos da biblioteca e utilizei impressão
# com duas casas decimais para ser algo mais limpo.
