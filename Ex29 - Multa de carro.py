# Exercício 29 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 para cada Km acima do limite.

velocidade = int(input('Digite a velocidade do carro: '))

if velocidade > 80:
    valor = (velocidade - 80) * 7
    print(f'\nVocê foi multado e o valor da multa é de R$ {valor:.2f}')
else:
    print('Parabéns, você estava trafegando de acordo com as regras de trânsito!')
