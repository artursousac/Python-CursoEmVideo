# Exercício 42. Refaça o EX45 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: - Equilátero: Todos os lados iguais. - Isósceles: Dois lados iguais.
# - Escaleno: Todos os lados diferentes.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

reta1 = float(input('Digite o comprimento de uma reta: '))
reta2 = float(input('Digite o comprimento de outra reta: '))
reta3 = float(input('Digite o comprimento de outra reta: '))

if reta3 > reta1 and reta3 > reta2:
    maior = reta3
    menor1 = reta1
    menor2 = reta2
elif reta1 > reta2 and reta1 > reta3:
    maior = reta1
    menor1 = reta2
    menor2 = reta3
elif reta2 > reta1 and reta2 > reta3:
    maior = reta2
    menor1 = reta1
    menor2 = reta3
elif reta1 == reta2 and reta1 > reta3:
    maior = reta1
    menor1 = reta2
    menor2 = reta3
elif reta2 == reta3 and reta2 > reta1:
    maior = reta2
    menor1 = reta3
    menor2 = reta1

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

if (menor1 + menor2) > maior:
    if reta2 == reta1 == reta3:
        print('\nÉ possível formar um triângulo equilátero!')
    elif reta2 == reta1 or reta2 == reta3 or reta1 == reta3:
        print('É possível formar um triângulo isósceles!')
    else:
        print('É possível formar um triângulo escaleno!')
else:
    print('Não é possível a formação de um triângulo com estas medidas!')
