# Exercício 15 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado. #

print('\nEsse programa funcionará de modo que você nos fornece o Km percorrido do carro que alugou e a quantidade de dias que esteve alugado e o programa lhe fornece o preço a se pagar!')

km = float(input('\nDigite a quantidade de Km percorrido com o carro alugado: '))
dias = int(input('Digite qual a duração, em dias, do aluguel do carro: '))

preco = (dias * 60) + (km * 0.15)

print(f'\nO preço total a ser pago, no aluguel deste carro, será de: R$ {preco:.2f}')
