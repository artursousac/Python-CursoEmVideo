# Exercício 58. Melhore o jogo do DESAFIO028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('\033[1;31mBEM-VINDO AO JOGO DA ADIVINHAÇÃO. NESTE JOGO A MÁQUINA IRÁ PENSAR EM UM NÚMERO DE 0 A 10 E VOCÊ TENTARÁ ADIVINHAR. VAMOS JOGAR?\033[m')

resposta = 'não'
erro = 0

while resposta == 'não':
  numeromaquina = randint(0,10)
  numero = input('Digite um número de 0 a 10: ').strip()
  while not numero.isnumeric():
    print('\033[1;31mDIGITE UM NÚMERO VÁLIDO DENTRO DO INTERVALO DE 0 A 10!!!\033[m')
    numero = input('Digite um número de 0 a 10: ').strip()
  numero = int(numero)
  while 0 > numero > 10:
    print('\033[1;31mDIGITE UM NÚMERO VÁLIDO DENTRO DO INTERVALO DE 0 A 10!!!\033[m')
    numero = input('Digite um número de 0 a 10: ').strip()
  if numero != numeromaquina:
    erro += 1
    resposta = 'não'
    print(f'\033[1;31mQue pena, você errou\033[m. O número que a máquina pensou foi o \033[1;31m{numeromaquina}\033[m. Tente novamente!!!')
  if numero == numeromaquina:
    resposta = 'sim'
    print(f'\033[1;32mParabéns, você acertou!\033[m\nQuantidades de erros: \033[1;31m{erro}\033[m')
