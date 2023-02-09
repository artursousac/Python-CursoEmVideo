# Exercício 14 - Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

celsius = float(input('\nDigite uma temperatura em grau celsius que você deseja converter para Fahrenheit: '))
fahrenheit = ((9 * celsius) / 5) + 32

print(f'\nA temperatura, convertida para fahrenheit, é de: {fahrenheit}°F')
