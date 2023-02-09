# Exercício 49. Refaça o DESAFIO009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

numero = int(input('Digite um número que deseja descobrir a tabuada: '))

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')
for c in range (1,11):
  numtab = numero * c
  print(f'{numero} x {c} = {numtab}')
