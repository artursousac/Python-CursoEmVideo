# Exercício 57. Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

print('\033[1;31mENTRADA DO USUÁRIO\033[m')
sexo = input('Digite o sexo de uma pessoa (M ou F): ').upper().strip()[0]

while sexo not in 'MF':
    print('\033[1;31mDIGITE UM SEXO VÁLIDO. SOMENTE AS LETRAS M ou F\033[m')
    sexo = input('Digite o sexo de uma pessoa (M ou F): ').upper().strip()[0]

if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

print(f'{sexo} foi o sexo escolhido!')
