# Exercício 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto #

print('\nEste programa serve para ler o preço de um produto e aplicar um desconto de acordo com a necessidade.')

Valor = float(input('\nDigite o valor do produto: '))
PorcentoDesconto = float(input('Digite a porcentagem de desconto deste produto: '))
Desconto = Valor * (PorcentoDesconto/100)
ValorDesconto = Valor - Desconto

print(f'\nO preço deste produto, com o desconto de loja aplicado, é de R$ {ValorDesconto:.2f}')

