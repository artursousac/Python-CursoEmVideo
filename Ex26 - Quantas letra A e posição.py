# Exercício 26 - Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A"; Em que posição ela aparece a primeira vez; Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ')

letraA = frase.upper().count('A')
posicaouma = frase.upper().find('A')
posicaoultima = frase.upper().rfind('A')

print(f'\n- A quantidade de vezes que a letra "A" aparece é de {letraA} vezes!\n- A letra "A" aparece pela primeira vez na posição {posicaouma}! *Vale destacar que a primeira letra da frase é a posição 0.\n- A letra "A" aparece pela última vez na posição {posicaoultima}!')
