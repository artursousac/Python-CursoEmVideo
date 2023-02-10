# Aula17. Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
# As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

"""
Diferente das tuplas, que são imutáveis, as Listas são mutáveis e podem ser adicionados elementos na lista com o comando.append

Outra forma de manipular listas é com o comando del nome.[0] ou então com o comando nome.remove('') e, também, o comando nome.pop(), este por ultimo
irá removar o último elemento da lista e retornar o valor retirado.

Outra forma de formar uma lista é utilizar: valores = list(range(4,11)), que irá criar uma lista chamada valores de tamanho sendo 6.
Caso use para esta lista [0,1,2,3,4,5] o comando valores.sort() o computador irá organizar a lista por ordem alfabética/numérica.

Outra função é o num.insert(posição, valor a ser adicionado), que irá adicionar um valor no meio da lista, aonde você desejar que seja adicionado.

a função num.remove() irá remover o valor que você colocou no (), irá remover somente a primeira ocorrência deste valor.

Caso tenha a = [2,3,4,7] e b = a. Depois eu alterar algo no b, ele irá mexer nas duas listas, pois o python faz uma ligação quando duas listas estão iguais.
Com a finalidade de criar uma cópia da lista, SEM nenhuma ligação, utilizar b = a[:]

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
Neste código, temos que o 'c' irá ser o valor 0, 1, 2... de acordo com as posições da lista e 'v' será o valor que está na posição.

"""


