# Exercício 13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

print('\nEste programa servirá para indicar qual o valor do salário de um funcionário após o aumento estipulado!')
Salario = float(input('\nDigite o salário atual do funcionário: '))
Aumento = float(input('Digite o valor, em porcentagem, do aumento desejado: '))

SalarioAumento = (Salario * (Aumento/100)) + Salario

print(f'\nO novo salário do funcionário, com o aumento citado, é de: R$ {SalarioAumento:.2f}')
