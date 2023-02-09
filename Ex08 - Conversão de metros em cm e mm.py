# Exercício 08 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = float(input('Digite um valor, em metros, que você deseja transformar em centímetros e em milímetros: '))
cent = valor*100
mili = valor*1000

print(f'O valor solicitado, em centímetros e em milímetros, respectivamente, é de: {cent:.2f} cm e {mili:.2f} mm')
