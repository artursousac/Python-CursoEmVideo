# Aula 16 — Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:  # comida funciona como se fosse aquele "c" e ele irá no "lanche" passar por todos os valores. Ou seja, se lanche fosse 0, 1, 2, 3, ele iria fazer como se fosse um c in range (0,4), primeiro fazer o 0, depois voltaria
    # Depois voltaria e fazeria o 1 e assim por diante. Como no lanche tem uma palavra, então ele faz cada palavra por vez.
    print(f'Eu vou comer {comida}')
print('Comi para caramba!')
'''

'''
Outra opção é utilizar for cont in range (0, len(lanche)):
                           print(f'Eu vou comer {lanche[cont]} na posição {cont})
Ou também utilizar.
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
'''

# print(sorted(lanche))  # sorted coloca a tupla em ordem, MAS NÃO ALTERA A TUPLA, POIS TUPLA É IMUTÁVEL.
# A soma de duas tuplas pode ser realizada para adicionar uma tupla na outra:
# a = (2, 5, 4). b = (5, 8, 1, 2). c = b + a (a ordem influência na ordem da tupla c).

'''
Nas tuplas é possível utilizar a função namedtuple da biblioteca collections.
Isto serve para criar classes dentro da tupla.
Tupla é mais usada para situações com classes diferentes, diferente da lista, que normalmente é mais homogenea.
Apesar de Tupla ser imutável, o que está dentro dela não é: por exemplo, podemos colocar uma lista em uma das posições
da Tupla e usar o append na lista ou remove, alterando a lista, porém a tupla permanece a mesma.
'''

'''
>>> from collections import namedtuple

>>> # Create a namedtuple type, Point
>>> Point = namedtuple("Point", "x y")
>>> issubclass(Point, tuple)
True

>>> # Instantiate the new type
>>> point = Point(2, 4)
>>> point
Point(x=2, y=4)

>>> # Dot notation to access coordinates
>>> point.x
2
>>> point.y
4

>>> # Indexing to access coordinates
>>> point[0]
2
>>> point[1]
4
'''

from collections import namedtuple
from time import sleep

c = 0

Dados = namedtuple('Dados', 'nome idade sexo doença')
dados = Dados([], [], [], [])
while True:
    print(f'\033[1;34m{c+1}º PACIENTE\033[m')
    contador = 0
    dados.nome.append(input(f'Digite o nome do {c+1}º paciente: ').strip().capitalize())
    for i in range(0, len(dados.nome[c])):
        if not dados.nome[c][i].isalpha():
            contador += 1
        if dados.nome[c][i] == ' ':
            contador -= 1
    while contador != 0:
        print('\033[1;31mDIGITE UM NOME VÁLIDO!!!\033[m')
        contador = 0
        del dados.nome[c]
        dados.nome.append(input(f'Digite o nome do {c+1}º paciente: ').strip().capitalize())
        for i in range(0, len(dados.nome[c])):
            if not dados.nome[c][i].isalpha():
                contador += 1
            if dados.nome[c][i] == ' ':
                contador -= 1
    dados.idade.append(input(f'Digite a idade do {c+1}º paciente: ').strip())
    while not dados.idade[c].isnumeric():
        print('\033[1;31mDIGITE UMA IDADE VÁLIDA\033[m')
        del dados.idade[c]
        dados.idade.append(input(f'Digite a idade do {c+1}º paciente: ').strip())
    dados.idade[c] = int(dados.idade[c])
    dados.sexo.append(input(f'Digite o sexo do {c+1}° paciente: ').strip().lower())
    while dados.sexo[c] not in ['masculino', 'feminino', 'm', 'f']:
        print('\033[1;31mDIGITE UM SEXO VÁLIDO!!!\033[m')
        del dados.sexo[c]
        dados.sexo.append(input(f'Digite o sexo do {c+1}° paciente: ').strip().lower())
    dados.doença.append(input(
        '\033[1;33mLISTA DE SINTOMAS\033[m\n\033[1;33m[1]\033[m - Dor nos seios + Caroço nos seios\n\033[1;33m[2]\033[m - Náusea, Sensação de fraqueza, Diarreia e Dor abdominal\n\033[1;33m[3]\033[m - '
        'Febre alta, Mal estar, Sensação de rigidez no abdômen, Dor atrás dos olhos e Manchas vermelhas pelo corpo\n\033[1;33m[4]\033[m - Falta de ar durante a noite e ritmo cardíaco acelerado\n\033[1;33m[5]\033[m - Tontura com Sensação de Desmaio\nEscolha um dos sintomas acima: '))
    while dados.doença[c] not in ['1', '2', '3', '4', '5']:
        print('\033[1;31mDIGITE UM NÚMERO DE 1 A 5 RELACIONADO AOS SINTOMAS LISTADOS!!!\033[m')
        del dados.doença[c]
        dados = Dados([], [], [], input(
            '\033[1;33mLISTA DE SINTOMAS\033[m\n\033[1;33m[1]\033[m - Dor nos seios + Caroço nos seios\n\033[1;33m[2]\033[m - Náusea, sensação de fraqueza, Diarreia e dor abdominal\n\033[1;33m[3]\033[m - '
            'Febre alta, Mal estar, Sensação de rigidez no abdômen, Dor atrás dos olhos e Manchas vermelhas pelo corpo\n\033[1;33m[4]\033[m - Falta de ar durante a noite e ritmo cardíaco acelerado\n\033[1;33m[5]\033[m - Tontura com Sensação de Desmaio\nEscolha um dos sintomas acima: '))
    c += 1
    print('\033[1;33m=-\033[m' * 60)
    resposta = input('\033[1;32mVocê deseja incluir mais algum paciente: \033[m').strip().lower()
    while resposta not in ['sim', 'não', 'nao']:
        print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA!!! SIM OU NÃO.\033[m')
        resposta = input('Você deseja incluir mais algum paciente: ').strip().lower()
    if resposta in ['nao', 'não']:
        print('\033[1;34mENTENDIDO. ESTAMOS ORGANIZANDO OS DADOS INFORMADOS E FORNECEREMOS UMA RESPOSTA PARA CADA PACIENTE.\033[m')
        print('\033[1;33m.')
        sleep(1)
        print('.')
        sleep(1)
        print('.\033[m')
        sleep(1)
        break
for i in range(0, c):
    print('\033[1;33m=-\033[m' * 60)
    print(f'\033[1;34m{i+1}° PACIENTE\033[m')
    if dados.doença[i] == '1' and dados.sexo[i] in ['f', 'feminino'] and dados.idade[i] in range(15, 120):
        print(f'Olá, {dados.nome[i]}\nDe acordo com as informações nos passado, você pode estar com algum problema relacionado às mamas.'
              f'Diante disso, com a finalidade de se precaver com relação ao câncer de mama, nós estamos marcando uma consulta presencial com um de'
              f'nossos médicos parceiros.')
        print('\033[1;34mDADOS DO PACIENTE\033[m')
        print(f'Nome: {dados.nome[i]}\nIdade: {dados.idade[i]}\nSexo: {dados.sexo[i]}\nSintomas: {dados.doença[i]}')
    elif dados.doença[i] == '1' and dados.sexo[i] in ['f', 'feminino', 'm', 'masculino'] and dados.idade[i] in range(0, 15):
        print(f'Olá, {dados.nome[i]}\nDe acordo com as informações nos passado, você não deve se preocupar fortemente com os sintomas, pois podem ser'
              f'normal devido a fase de crescimento. No entanto, caso persista por vários dias, além de incomodar mais que o normal, nos retorne'
              f'e marque uma consulta com um de nossos especialistas.')
        print('\033[1;34mDADOS DO PACIENTE\033[m')
        print(f'Nome: {dados.nome[i]}\nIdade: {dados.idade[i]}\nSexo: {dados.sexo[i]}\nSintomas: {dados.doença[i]}')
    elif dados.doença[i] == '1' and dados.sexo[i] in ['m', 'masculino'] and dados.idade[i] in range (15, 120):
        print(f'Olá, {dados.nome[i]}\nDe acordo com os dados informados, a chance de você ter um câncer de mama é menor, mas não nulas. Assim'
              f'é importante se cuidar e realizar exames por preucação. Iremos marcar uma consulta presencial para você com um de nossos médicos.')
        print('\033[1;34mDADOS DO PACIENTE\033[m')
        print(f'Nome: {dados.nome[i]}\nIdade: {dados.idade[i]}\nSexo: {dados.sexo[i]}\nSintomas: {dados.doença[i]}')
    elif dados.doença[i] == '2':
        print(f'Olá, {dados.nome[i]}\nPelo que você nos disse, estes podem ser um indicio de Infecção Alimentar. Procure um ponto de saúde para '
              f'melhor avaliação e cuidados.')
        print('\033[1;34mDADOS DO PACIENTE\033[m')
        print(f'Nome: {dados.nome[i]}\nIdade: {dados.idade[i]}\nSexo: {dados.sexo[i]}\nSintomas: {dados.doença[i]}')
    elif dados.doença[i] == '3':
        print(f'Olá, {dados.nome[i]}\nPara estes sintomas, a principal suspeita é você estar com \033[1;31mDengue\033[m. Tome bastante água e procure'
              f'um médico em caso de piora. Em alguns casos, é necessário urgência no atendimento devido a possibilidade de hemorragias. Cuidado!!!')
        print('\033[1;34mDADOS DO PACIENTE\033[m')
        print(f'Nome: {dados.nome[i]}\nIdade: {dados.idade[i]}\nSexo: {dados.sexo[i]}\nSintomas: {dados.doença[i]}')
    elif dados.doença[i] == '4':
        print(f'Olá, {dados.nome[i]}\nCom esta falta de ar e sintomas relatados, você pode estar com \033[1;31mAsma\033[m. Iremos marcar uma consulta'
              f'com um de nossos especialista para um diagnóstico mais preciso.')
        print('\033[1;34mDADOS DO PACIENTE\033[m')
        print(f'Nome: {dados.nome[i]}\nIdade: {dados.idade[i]}\nSexo: {dados.sexo[i]}\nSintomas: {dados.doença[i]}')
    elif dados.doença[i] == '5':
        print(f'Olá, {dados.nome[i]}\nVocê pode estar com pressão baixa. Procure comer algo que tenha açúcar, se deite em posição'
              f'confortável aguarde uma melhora. Em caso de vários minutos sem a situação melhorar, procure um atendimento médico.')
        print('\033[1;34mDADOS DO PACIENTE\033[m')
        print(f'Nome: {dados.nome[i]}\nIdade: {dados.idade[i]}\nSexo: {dados.sexo[i]}\nSintomas: {dados.doença[i]}')

'''
#if dados.idade in range(10, 41) and dados.sexo in ('F', 'Feminino', 'feminino', 'f') and dados.doença in ['2', 2]:
 #   print(f'Bem-vindo ao atendimento online, {dados.nome}!!!\nPercebi que sua idade é de {dados.idade} anos e você é uma mulher. Portanto, para esse sintoma você está com suspeita de \033[1;33mGRAVIDEZ\033[m')

#print(Dados('Artur', '23', 'Masculino', 'Estudante'))

#Existem essas opções para trabalhar com a tupla, tanto a primeira de criar uma outra variável dados ou a que já
#trabalha diretamente com a subclasse, gerando: nome=Artur, como resposta por exemplo.

'''