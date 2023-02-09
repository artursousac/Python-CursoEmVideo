# Exercício 43. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso. - Entre 18.5 e 25: Peso ideal. - 25 até 30: Sobrepeso. - 30 até 40: Obesidade. - Acima de 40: Obesidade mórbida.

from math import pow

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = (peso/pow(altura,2))

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

if imc < 18.5:
    print('\033[1;31mCUIDADO!\033[m Você está abaixo do peso ideal!')
elif 18.5 <= imc < 25:
    print('\033[1;32mPARABÉNS!\033[m Você está com o peso ideal!')
elif 25 <= imc < 30:
    print('\033[1;31mCUIDADO!\033[m Você está com sobrepeso. Procure mudar sua rotina!')
elif 30 <= imc < 40:
    print('\033[1;31mCUIDADO REDOBRADO!\033[m Você está com obesidade. Procure ajude médica!')
else:
    print('\033[1;31mATENÇÃO!\033[m Você está com Obesidade mórbida!!!')
