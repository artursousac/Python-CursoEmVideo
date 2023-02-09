# Exercício 75. Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

par = []
nove = 0
posicao3 = 0

#Outra forma é utilizar o próprio input dentro da tupla, por exemplo:
#tupla = (input('Digite um número: ), input('Digite um número: )...)
while True:
    num1 = input('Digite um número inteiro: ')
    if num1.isnumeric():
        num1 = int(num1)
        break
    else:
        print('\033[1;31mDIGITE UM NÚMERO INTEIRO VÁLIDO!!!\033[m')
while True:
    num2 = input('Digite um número inteiro: ')
    if num2.isnumeric():
        num2 = int(num2)
        break
    else:
        print('\033[1;31mDIGITE UM NÚMERO INTEIRO VÁLIDO!!!\033[m')
while True:
    num3 = input('Digite um número inteiro: ')
    if num3.isnumeric():
        num3 = int(num3)
        break
    else:
        print('\033[1;31mDIGITE UM NÚMERO INTEIRO VÁLIDO!!!\033[m')
while True:
    num4 = input('Digite um número inteiro: ')
    if num4.isnumeric():
        num4 = int(num4)
        break
    else:
        print('\033[1;31mDIGITE UM NÚMERO INTEIRO VÁLIDO!!!\033[m')
tupla = (num1, num2, num3, num4)
tres = 0
for c in range(0, len(tupla)):
    if tupla[c] % 2 == 0:
        par.append(tupla[c])
    if tupla[c] == 9:
        nove += 1
    if tupla[c] == 3:
        tres += 1
if tres > 0:
    tres = tupla.index(3)
print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

if nove > 0:
    print(f'O valor nove aparece \033[1;32m{nove}\033[m vezes.')
if nove == 0:
    print('\033[1;31mNão\033[m foi digitado o valor nove.')
if tres > 0:
    print(f'O valor três apareceu a primeira vez na posição \033[1;32m{tres+1}\033[m.')
elif tres <= 0:
    print('\033[1;31mNão\033[m foi digitado o valor três.')
if len(par) > 0:
    print('Os números pares digitados foram o', end=' ')
    for c in range(0, len(par)):
        print(f'\033[1;32m{par[c]}\033[m', end=' ')
elif len(par) == 0:
    print('Não foi digitado \033[1;31mnenhum\033[m número par.')
