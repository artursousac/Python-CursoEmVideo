# Exercício 63. Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.

print('\033[1;31mENTRADA DO USUÁRIO\033[m')

numero = input('Digite um número inteiro qualquer: ')

while not numero.isnumeric() or numero == '0':
    print('\033[1;31mDIGITE UM NÚMERO INTEIRO VÁLIDO!!!\033[m')
    numero = input('Digite um número inteiro qualquer: ')
numero = int(numero)

sequencia = 2
f = [1, 1]

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')
print('0 1', end= ' ')

while sequencia < numero+2:
    f.append(f[sequencia-1] + f[sequencia-2])
    sequencia += 1
    print(f[sequencia-2], end=' ')
