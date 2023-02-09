# Exercício 03 #

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

num1 = float(input('Agora, por favor, digite um número: '))
num2 = float(input('Digite outro número: '))
soma = num1 + num2

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

print(f'A soma entre os números {num1:.2f} e {num2:.2f} é {soma:.2f}')
