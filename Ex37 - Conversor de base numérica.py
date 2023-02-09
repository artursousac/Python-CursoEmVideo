# Exercício 37. Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: - 1 Para binário; - 2 Para octal; - 3 Para hexadecimal.
# Pesquisar como transformar um valor para essas bases numéricas. O Python faz isso sozinho.

print('\033[1;31mENTRADAS DO USUÁRIO\033[0;m')

numero = int(input('Digite um número inteiro: '))

escolha = int(input('Qual será a base de conversão?\n\033[1;31m[1]\033[0;m - Binário\n\033[1;31m[2]\033[0;m - Octal\n\033[1;31m[3]\033[0;m - Hexadecimal\nEscolha:'))

print('\033[1;33m-=\033[0,m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[0;m')

if escolha == 1:
    binario = bin(numero)[2:]
    print(f'O número inteiro {numero} transformado em Binário é igual a {binario}')
elif escolha == 2:
    octal = oct(numero)[2:]
    print(f'O número inteiro {numero} transformado em Octal é igual a {octal}')
elif escolha == 3:
    hexadecimal = hex(numero)[2:]
    print(f'O número inteiro {numero} transformado em Hexadecimal é igual a {hexadecimal}')
else:
    print('\033[31mOpção Inválida!!!\033[m')
