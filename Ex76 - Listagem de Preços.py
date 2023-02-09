# Exercício 76. Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('\033[1;33m=-\033[m' * 20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('\033[1;33m=-\033[m' * 20)

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90
            )
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:.<30}', end='\033[1;32mR$ \033[m')
    print(f'\033[1;32m{listagem[c+1]:.2f}\033[m')
