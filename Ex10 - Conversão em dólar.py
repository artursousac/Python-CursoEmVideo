# Exercício 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Doláres ela pode comprar US$ 1.00 = R$ 3.27

dinheiro = float(input('Digite quanto você tem de dinheiro na carteira: '))
conv = 1/3.27
dolares = dinheiro*conv

print(f'Caso queira converter seu dinheiro para dólar, o valor atual seria de: US$ {dolares:.2f}')
