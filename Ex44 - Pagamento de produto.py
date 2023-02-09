# Exercício 44. Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À Vista dinheiro/cheque: 10% de desconto. - À Vista no cartão: 5% de desconto. - Em até 2x no cartão: preço normal. - 3x ou mais no cartão: 20% de Juros.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

preconormal = float(input('Digite o preço do normal do produto: R$ '))
pagamento = int(input('OPÇÕES DE PAGAMENTO:\n\033[1;31m[1]\033[m - À Vista no dinheiro ou cheque.\n\033[1;31m[2]\033[m - À Vista no cartão.\n\033[1;31m[3]\033[m - Em até 2x no cartão.\n\033[1;31m[4]\033[m - 3x ou mais no cartão.\nEscolha a condição de pagamento para este produto: '))

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

if pagamento == 1:
    valor = preconormal * 0.9
    print(f'Para pagamento à vista no dinheiro ou cheque você receberá 10% de desconto. Portanto, o valor a ser pago será de R$ {valor}.')
elif pagamento == 2:
    valor = preconormal * 0.95
    print(f'Para pagamento à vista no cartão você receberá 5% de desconto. Portanto, o valor a ser pago será de R$ {valor}.')
elif pagamento == 3:
    valor = preconormal
    print(f'Para pagamento no cartão em até 2x você não recebe desconto. Assim, o valor a ser pago será de R$ {valor}.')
elif pagamento == 4:
    valor = preconormal * 1.20
    print(f'Para pagamento no cartão de 3x ou mais você terá que pagar um juros de 20%. Logo, o valor total a ser pago será de R$ {valor}')
