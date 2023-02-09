# Exercício 39. Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade: — Se ele ainda vai se alistar ao serviço militar. - Se é a hora de se alistar. - Se já
# passou do tempo do alistamento. O seu programa deverá mostrar o tempo que falta ou que passou do prazo.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

ano = int(input('Digite o seu ano de nascimento: '))

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

if ano > 2004:
  diferenca = ano - 2004
  if diferenca == 1:
      print(f'Você ainda não necessita se alistar ao serviço militar! Falta {diferenca} ano!')
  else:
      print(f'Você ainda não necessita se alistar ao serviço militar! Faltam {diferenca} anos!')
elif ano == 2004:
    print('Chegou sua hora de se alistar!')
else:
    diferenca = 2004 - ano
    if diferenca == 1:
        print(f'Você passou do tempo do alistamento! Deveria ter se alistado há {diferenca} ano!')
    else:
        print(f'Você passou do tempo do alistamento! Deveria ter se alistado há {diferenca} anos!')
