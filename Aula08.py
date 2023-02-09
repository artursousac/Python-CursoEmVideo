# Teste das informações da aula 08
# Ceil arredonda um número para "cima" e o Floor arredonda para "baixo".
# Sqrt fornece a raíz quadrada de um número e a Isqrt devolve a raíz quadrada, já transformando em um número inteiro.
# Pow eleva um número a tal potência, onde (3,2) significa 3 elevado a 2.
# Outra biblioteca interessante é a random, onde gera número aleatórios para o programa com o random.random, além de poder definir de 1 a 10 com o random.randint, por exemplo.
# A biblioteca emoji retorna os emojis. Utilizando o comando emoji.emojize ('Frase a ser citada e entre ":" o emoji e , language='alias'). Notar que, a linguagem padrão é inglês, caso queira utilizar outra, colocar ", language='pt'.


import math
import random
import emoji

num = random.randint(1, 100)
print(num)
print(math.isqrt(random.randint(0, 10000000)))
print(emoji.emojize('Melado :red_heart:', language='alias'))
