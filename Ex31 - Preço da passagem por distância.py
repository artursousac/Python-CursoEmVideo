# Exercício 31. Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

distancia = float(input('Digite a distância da viagem em km: '))

if distancia > 200:
    passagem = distancia * 0.45
    print(f'\nO preço da passagem é de R$ {passagem:.2f}')
else:
    passagem = distancia * 0.50
    print(f'\nO preço da passagem é de R$ {passagem:.2f}')
