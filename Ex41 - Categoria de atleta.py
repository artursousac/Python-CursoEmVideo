# Exercício 41. A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM. - Até 14 anos: INFANTIL. - Até 19 anos: JUNIOR. - Até 20 anos: SÊNIOR. - Acima: MASTER.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

anonasc = int(input('Digite seu ano de nascimento: '))
if anonasc > 2023:
    print('Por favor, digite um ano de nascimento válido!')
else:
    idade = 2023 - anonasc

    print('\033[1;33m=-\033[m' * 60)
    print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

    if idade <= 9:
        print(f'De acordo com a Confederação Nacional de Natação, sua categoria será a MIRIM!')
    elif 9 < idade <= 14:
        print(f'De acordo com a Confederação Nacional de Natação, sua categoria será a INFANTIL!')
    elif 14 < idade <= 19:
        print(f'De acordo com a Confederação Nacional de Natação, sua categoria será a JUNIOR!')
    elif idade == 20:
        print(f'De acordo com a Confederação Nacional de Natação, sua categoria será a SÊNIOR!')
    else:
        print(f'De acordo com a Confederação Nacional de Natação, sua categoria será a MASTER!')
