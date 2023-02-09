# Exercício 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m² #

print('\nEste programa será utilizado para calcular a área de uma parede e a quantidade de tinta necessária para pintá-la!\n')
LarguraParede = float(input('Digite a largura da parede em metros: '))
AlturaParede = float(input('Digite a altura da parede em metros: '))
AreaParede = LarguraParede * AlturaParede
QuantidadeTinta = AreaParede * 0.5

print(f'\nA área da parede é de {AreaParede:.2f}m² e a quantidade necessária de tinta para pintá-la é de {QuantidadeTinta:.2f}L')
