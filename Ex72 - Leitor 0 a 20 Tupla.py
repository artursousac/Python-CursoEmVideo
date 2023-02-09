# Exercício 72. Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
print('\033[1;33m=-\033[m' * 60)
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
            )

numero = input('Digite um número: ').strip()
while not numero.isnumeric():
    print('\033[1;31mDIGITE UM NÚMERO VÁLIDO\033[m')
    numero = input('Digite um número: ').strip()
numero = int(numero)
while numero not in range(0, 21):
    print('\033[1;31mDIGITE UM NÚMERO VÁLIDO\033[m')
    numero = input('Digite um número: ').strip()
    while not numero.isnumeric():
        print('\033[1;31mDIGITE UM NÚMERO VÁLIDO\033[m')
        numero = input('Digite um número: ').strip()
    numero = int(numero)
print(f'O número digitado foi o \033[1;32m{contagem[numero]}\033[m')
