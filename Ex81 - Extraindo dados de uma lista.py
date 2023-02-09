# Exercício 81. Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

valores = []
c = 0
valor5 = 'não foi'

while True:
    print('\033[1;33m=-\033[m' * 60)
    valores.append(input('Digite um número inteiro maior ou igual a 0: ').strip())
    while not valores[c].isnumeric():
        print('\033[1;31mDIGITE UM NÚMERO VÁLIDO!!!\033[m')
        del valores[c]
        valores.append(input('Digite um número inteiro maior ou igual a 0: ').strip())
    valores[c] = int(valores[c])
    if valores[c] == 5:
        valor5 = 'foi'
    resposta = input('\033[1;34mDeseja digitar mais números? (Sim ou Não): \033[m').strip().lower()
    while resposta not in ['não', 'nao', 'n', 'sim', 's']:
        print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA. SIM OU NÃO!!!\033[m')
        resposta = input('\033[1;34mDeseja digitar mais números? (Sim ou Não): \033[m').strip().lower()
    if resposta in ['não', 'nao', 'n']:
        print('\033[1;33m=-\033[m' * 60)
        break
    c += 1

valores.sort(reverse=True)

print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

print(f'\033[1;32m{c+1}\033[m Números foram digitados.'
      f'\nA lista de valores, ordenada de ordem decrescente é: \033[1;32m{valores}\033[m'
      f'\nO valor 5 \033[1;32m{valor5}\033[m digitado.')
