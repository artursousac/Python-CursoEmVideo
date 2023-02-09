# Exercício 36. Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

#Primeiramente iremos fazer o programa ler o valor das variáveis deste problema.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

casa = float(input('Digite o valor da casa que deseja comprar: R$').strip()) #Estou usando o ‘strip’ para retirar os espaços, caso o usuário digite um espaço antes ou no final.
salario = float(input('Digite o seu salário mensal: R$').strip())
anos = int(input('Deseja pagar em quantos ano: ').strip())

#Irei utilizar os dados fornecidos para descobrir quanto custa 30% do salário do usuário, além da prestação mensal que ficará a casa!

salario30 = salario*0.3
prestacaomensal = casa/(anos*12)

#Após isso, estou utilizando as estruturas de condição, pois existem duas possibilidades (Aprovar ou Reprovar o empréstimo)
#Também, irei utilizar uma mudança de cor nas palavras Negado e Aprovado, para deixar claro qual foi o resultado.

print('\033[1;33m-=\033[0,m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

if prestacaomensal > 0.3*salario:
    print(f'O empréstimo será \033[1;31mnegado\033[0;m, pois a prestação mensal (R$ {prestacaomensal:.2f}) é maior que 30% do seu salário (R$ {salario30:.2f}).')
else:
    print(f'O empréstimo será \033[1;32aprovado!\033[0;m A prestação mensal será de R$ {prestacaomensal:.2f}')
