# Exercício 23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex: 1834. U = 1; D = 3; C = 8; M = 1

numero = input('Digite um número: ')

Unidade = (numero[len(numero)-1:])
Dezena = (numero[len(numero)-2:len(numero)-1])
Centena = (numero[len(numero)-3:len(numero)-2])
Milhar = (numero[len(numero)-4:len(numero)-3])

print(f'Para o número {numero}, temos os seguintes dígitos: \nUnidade = {Unidade}\nDezena = {Dezena}\nCentena = {Centena}\nMilhar = {Milhar}')

'''A maneira correta de ser feita é por meio da matemática, utilizando divisão inteira e tirando o resto de 10:
numero = input('Digite um número: ')

Unidade = numero // 1 % 10
Dezena = numero // 10 % 10
Centena = numero // 100 % 10
Milhar = numero // 1000 % 10

Vale destacar que "//" faz uma divisão e retorna o valor inteiro da divisão e "%" tira o módulo/resto.
'''
