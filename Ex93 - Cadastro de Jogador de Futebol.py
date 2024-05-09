# Exercício 93. Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

contador = 0
start = 0
jogador = {}
#Nome do Jogador
while contador > 0 or start == 0:
    if contador > 0 and start != 0:
        print('\033[1;31mDIGITE O NOME DE UM JOGADOR VÁLIDO (CUIDADO COM ESPAÇOS DOBRADOS E SÍMBOLOS)\033[m')
    start = 1
    nome = input('Digite o nome do jogador de futebol: ').strip().title()
    contador = 0
    for i in range(0, len(nome)):
        if not nome[i].isalpha():
            contador += 1
        if nome[i] == ' ':
            contador -= 1
        if (len(nome.split()) - nome.count(' ')) != 1:
            contador += 1
jogador['Nome'] = nome

#Quantidades de Partidas
quantidadesPartidas = input('Digite quantas partidas o jogador jogou: ').strip()
while not quantidadesPartidas.isnumeric():
    print('\033[1;31mDIGITE UMA QUANTIDADE DE PARTIDAS VÁLIDA. MAIOR OU IGUAL A 0!!!\033[m')
    quantidadesPartidas = input('Digite quantas partidas o jogador jogou: ').strip()
quantidadesPartidas = int(quantidadesPartidas)
jogador['Partidas Jogadas'] = quantidadesPartidas

#Gols feitos em cada partida jogada e soma de gols
gols = []
somaGols = 0
for i in range (0, quantidadesPartidas):
    quantidadeGols = input(f'Digite quantos gols o jogador fez na {i+1}° partida: ').strip()
    while not quantidadeGols.isnumeric():
        print('\033[1;31mDIGITE UM VALOR NUMÉRICO MAIOR OU IGUAL A 0!!!\033[m')
        quantidadeGols = input(f'Digite quantos gols o jogador fez na {i+1}° partida: ').strip()
    quantidadeGols = int(quantidadeGols)
    gols.append(quantidadeGols)
    somaGols += quantidadeGols
jogador['Gols'] = gols
jogador['Total de Gols'] = somaGols

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

#Print do resultado. Vale observar que poderiamos utilizar for k, v in jogador.items. Porém, deste jeito feito ficou melhor para visualização de resultado.
print(f'Nome = {jogador["Nome"]:}\n'
      f'Partidas Jogadas = {jogador["Partidas Jogadas"]}')
for i in range (0, quantidadesPartidas):
    print(f'O jogador fez {jogador["Gols"][i]} gols na {i+1}° partida')
print(f'Total de Gols = {jogador["Total de Gols"]}')

