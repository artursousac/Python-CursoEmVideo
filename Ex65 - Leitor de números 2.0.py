# Exercício 65. Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

resposta = 'sim'
soma = 0
menor = float("INF")
maior = 0
quantidade = 0

while resposta not in ['não', 'nao']:
    numero = input('Digite um número inteiro: ').strip()
    while not numero.isnumeric():
        print('\033[1;31mDIGITE UM NÚMERO INTEIRO VÁLIDO!!!\033[m')
        numero = input('Digite um número inteiro: ').strip()
    numero = int(numero)
    soma += numero
    quantidade += 1
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero
    resposta = input('\033[1;34mVocê deseja continuar digitando valores? (Sim ou Não): \033[m').lower().strip()
    while resposta not in ['sim', 'não', 'nao']:
        print('\033[1;31mDIGITE UMA OPÇÃO VÁLIDA: SIM OU NÃO!!!\033[m')
        resposta = input('Você deseja continuar digitando valores? (Sim ou Não): ').lower().strip()

media = soma/quantidade

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')
print(f'A \033[1;32mmédia\033[m dos valores digitados é de \033[1;32m{media:.2f}\033[m.\nO \033[1;32mmaior\033[m valor digitado foi \033[1;32m{maior}\033[m.\nO \033[1;32mmenor\033[m valor digitado foi \033[1;32m{menor}\033[m.')
