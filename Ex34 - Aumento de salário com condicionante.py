# Exercício 34. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para inferiores ou iguals,
# o aumento é de 15%.

salario = float(input('Digite seu salário: '))

if salario > 1250:
    aumento = salario * 0.1
    salarionovo = salario + aumento
    print(
        f'\nSeu aumento salarial será de 10%, o que corresponde a R$ {aumento:.2f}. Portanto, seu novo salário será de R$ {salarionovo:.2f}')
else:
    aumento = salario * 0.15
    salarionovo = salario + aumento
    print(
        f'\nSeu aumento salarial será de 15%, o que corresponde a R$ {aumento:.2f}. Portanto, seu novo salário será de R$ {salarionovo:.2f}')
