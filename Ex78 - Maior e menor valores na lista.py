# Exercício 78. Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

valores = []
maior = 0
menor = float("INF")
posicaomaior = []
posicaomenor = []


for c in range(0,5):
    valores.append(input(f'Digite o {c+1}° valor numérico maior ou igual a 0: ').strip())
    while not valores[c].isnumeric():
        print('\033[1;31mDIGITE UM VALOR NUMÉRICO VÁLIDO!!!\033[m')
        del valores[c]
        valores.append(input(f'Digite o {c + 1}° valor numérico maior ou igual a 0: ').strip())
    valores[c] = int(valores[c])
for c in range(0,5):
    if valores[c] == max(valores):
        posicaomaior.append(c+1)
    if valores[c] == min(valores):
        posicaomenor.append(c+1)
maior = max(valores)
menor = min(valores)


print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

if len(posicaomaior) == 1:
    print(f'O maior valor digitado foi o \033[1;32m{maior}\033[m e se encontra na posição \033[1;32m{posicaomaior[0]}\033[m da lista de números digitados.', end= ' ')
elif len(posicaomaior) > 1:
    print(f'O maior valor digitado foi o \033[1;32m{maior}\033[m e se encontra nas posições', end= ' ')
    for c in range(0, len(posicaomaior)):
        print(f'\033[1;32m{posicaomaior[c]}', end= '... \033[m')
if len(posicaomenor) == 1:
    print(f'\nO menor valor digitado foi o \033[1;32m{menor}\033[m e se encontra na posição \033[1;32m{posicaomenor[0]}\033[m da lista de números digitados.', end= ' ')
elif len(posicaomenor) > 1:
    print(f'\nO menor valor digitado foi o \033[1;32m{menor}\033[m e se encontra nas posições', end= ' ')
    for c in range(0, len(posicaomenor)):
        print(f'\033[1;32m{posicaomenor[c]}', end= '... \033[m')
