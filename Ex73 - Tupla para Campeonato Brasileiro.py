# Exercício 73. Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação
# Depois mostre: A) Apenas os 5 primeiros colocados. B) Os últimos 4 colocados da tabela. C) Uma lista com os times em ordem alfabética.
# C) Uma lista com os times em ordem alfabética D) Em que posição na tabela está o time do Goiás.

print('\033[1;31mCAMPEONATO BRASILEIRO DE FUTEBOL 2022\033[m')

classificacao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athlético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo',
                 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude'
                 )

primeiros5 = []
ultimos4 = []
alfabeticos = sorted(classificacao)
goias = classificacao.index('Goiás') + 1
for c in range(0, 5):
    primeiros5.append(classificacao[c])
for c in range(-4, 0):
    ultimos4.append(classificacao[c])

print(f'\033[1;31m*\033[m Os 5 primeiros colocados do brasileiro de 2022, em ordem do 1° para o 5°, foram: {primeiros5}')
print(f'\033[1;31m*\033[m Os últimos 4 colocados do brasileiro de 2022, em ordem do 17° para o 20°, foram: {ultimos4}')
print(f'\033[1;31m*\033[m A classificação em ordem alfabética pode ser dada por: {alfabeticos}')
print(f'\033[1;31m*\033[m O Goiás terminou na {goias}º posição.')
