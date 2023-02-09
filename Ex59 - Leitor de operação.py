# Exercício 59. Crie um programa que leia dois valores e mostre um menu na tela: [1] Somar [2] Multiplicar [3] Maior [4] Novos Números [5] Sair do programa. Seu programa deverá realizar
# a operação solicitada em cada caso.

from time import sleep
resposta = 0

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

n1 = input('Digite um valor: ').strip()
while not n1.isnumeric():
  print('\033[1;31mDIGITE UM VALOR NÚMERICO VÁLIDO!!!\033[m')
  n1 = input('Digite um valor: ').strip()
n1 = float(n1)
n2 = input('Digite outro valor: ').strip()
while not n2.isnumeric():
  print('\033[1;31mDIGITE UM VALOR NUMÉRICO VÁLIDO!!!\033[m')
  n2 = input('Digite outro valor: ').strip()
n2 = float(n2)

while resposta != '5':
  sleep(1)
  resposta = input('Agora escolha o que deseja realizar com os dois números digitados:\n\033[1;33m[1]\033[m - Somar\n\033[1;33m[2]\033[m - Multiplicar\n\033[1;33m[3]\033[m - Maior\n\033[1;33m[4]\033[m - Novos Números\n\033[1;33m[5]\033[m - Sair do Programa\nEscolha: ').strip()
  while not resposta.isnumeric():
    print('\033[1;31mSELEÇÃO INVÁLIDA. ESCOLHA UMA DAS OPÇÕES LISTADAS ABAIXO!!!\033[m')
    resposta = input('Agora escolha o que deseja realizar com os dois números digitados:\n\033[1;33m[1]\033[m - Somar\n\033[1;33m[2]\033[m - Multiplicar\n\033[1;33m[3]\033[m - Maior\n\033[1;33m[4]\033[m - Novos Números\n\033[1;33m[5]\033[m - Sair do Programa\nEscolha: ').strip()
  respostaint = int(resposta)
  while respostaint > 5 or respostaint < 1:
      print('\033[1;31mSELEÇÃO INVÁLIDA. ESCOLHA UMA DAS OPÇÕES LISTADAS ABAIXO!!!\033[m')
      resposta = input('Agora escolha o que deseja realizar com os dois números digitados:\n\033[1;33m[1]\033[m - Somar\n\033[1;33m[2]\033[m - Multiplicar\n\033[1;33m[3]\033[m - Maior\n\033[1;33m[4]\033[m - Novos Números\n\033[1;33m[5]\033[m - Sair do Programa\nEscolha: ').strip()
      while not resposta.isnumeric():
        print('\033[1;31mSELEÇÃO INVÁLIDA. ESCOLHA UMA DAS OPÇÕES LISTADAS ABAIXO!!!\033[m')
        resposta = input('Agora escolha o que deseja realizar com os dois números digitados:\n\033[1;33m[1]\033[m - Somar\n\033[1;33m[2]\033[m - Multiplicar\n\033[1;33m[3]\033[m - Maior\n\033[1;33m[4]\033[m - Novos Números\n\033[1;33m[5]\033[m - Sair do Programa\nEscolha: ').strip()
      respostaint = int(resposta)
  if resposta == '1':
    soma = n1+n2
    print('\033[1;33m=-\033[m' * 60)
    print(f'A soma dos números \033[1;32m{n1}\033[m e \033[1;32m{n2}\033[m é igual a \033[1;32m{soma}\033[m')
    print('\033[1;33m=-\033[m' * 60)
  elif resposta == '2':
    multiplicacao = n1 * n2
    print('\033[1;33m=-\033[m' * 60)
    print(f'A multiplicação dos números \033[1;32m{n1}\033[m e \033[1;32m{n2}\033[m é igual a \033[1;32m{multiplicacao}\033[m')
    print('\033[1;33m=-\033[m' * 60)
  elif resposta == '3':
    if n1>n2:
      maior = n1
    elif n2>n1:
      maior = n2
    elif n1 == n2:
      maior = n1
    print('\033[1;33m=-\033[m' * 60)
    print(f'O maior número entre \033[1;32m{n1}\033[m e \033[1;32m{n2}\033[m é \033[1;32m{maior}\033[m')
    print('\033[1;33m=-\033[m' * 60)
  elif resposta == '4':
    print('\033[1;33mCOMO SOLICITADO, IREMOS REINICIAR OS NÚMEROS PARA QUE VOCê DIGITE NOVAMENTE DOIS NÚMEROS!!!\033[m')
    n1 = input('Digite um valor: ').strip()
    while not n1.isnumeric():
      print('\033[1;31mDIGITE UM VALOR NÚMERICO VÁLIDO!!!\033[m')
      n1 = input('Digite um valor: ').strip()
    n1 = float(n1)
    n2 = input('Digite outro valor: ').strip()
    while not n2.isnumeric():
      print('\033[1;31mDIGITE UM VALOR NUMÉRICO VÁLIDO!!!\033[m')
      n2 = input('Digite outro valor: ').strip()
    n2 = float(n2)
  elif resposta == '5':
    print('\033[1;33mSAINDO DO PROGRAMA!!!')
    sleep(1)
    print('...')
    sleep(1)
    print('\033[1;31mFIM DO PROGRAMA!!!\033[m')
