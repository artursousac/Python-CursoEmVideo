# Exercício 77. Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

from time import sleep

print(f'\033[1;31m{"DETECTOR DE VOGAIS":^120}\033[m')
print('\033[1;33m=-\033[m' * 60)
print('\033[1;34mLISTA DE PALAVRAS\033[m')

listapalavras = ('Casaco', 'Sanduiche', 'Cenoura', 'Sabia',
                 'Frango', 'Desodorante', 'Sundae', 'Carro'
                 )

for palavra in listapalavras:
    print(f'\nA palavra {palavra} possui as vogais ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'\033[1;32m{letra}\033[m', end=' ')

print('\n\n\033[1;31mFINALIZANDO CÓDIGO\033[m\n\033[1;33m.', end=' ')
sleep(1)
print('.', end=' ')
sleep(1)
print('.', end=' ')
sleep(1)
print('\n\033[1;31mFINALIZADO COM SUCESSO\033[m')
