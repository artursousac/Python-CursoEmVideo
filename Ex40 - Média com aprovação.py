# Exercício 40. Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, conforme a média atingida:
# — Média abaixo de 5.0: REPROVADO. - Média entre 5.0 e 6.9: RECUPERAÇÃO. - Média 7.0 ou superior: APROVADO.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

if media < 5:
    print(f'\033[1;31mREPROVADO!\033[m Estude mais, pois sua média foi de {media:.2f}.')
elif 5 <= media < 7:
    print(f'Sua média foi de {media:.2f}, logo você irá para a \033[1;33mRECUPERAÇÃO\033[m')
else:
    print(f'Parabéns, você foi \033[1;32mAPROVADO\033[m com média de {media:.2f}')
