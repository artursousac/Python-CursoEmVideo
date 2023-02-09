# Exercício 35. Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Digite o comprimento de uma reta: '))
reta2 = float(input('Digite o comprimento de outra reta: '))
reta3 = float(input('Digite o comprimento de outra reta: '))

if reta3 > reta1 and reta3 > reta2:
    maior = reta3
    menor1 = reta1
    menor2 = reta2
elif reta1 > reta2 and reta1 > reta3:
    maior = reta1
    menor1 = reta2
    menor2 = reta3
elif reta2 > reta1 and reta2 > reta3:
    maior = reta2
    menor1 = reta1
    menor2 = reta3
elif reta1 == reta2 and reta1 > reta3:
    maior = reta1
    menor1 = reta2
    menor2 = reta3
elif reta2 == reta3 and reta2 > reta1:
    maior = reta2
    menor1 = reta3
    menor2 = reta1


if (menor1 + menor2) > maior:
  print('\nÉ possível formar um triângulo!')
else:
  print('Não é possível a formação de um triângulo com estas medidas!')
