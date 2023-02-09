# Exercício 70. Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar. No final mostre: A) Qual é o total gasto na compra. B) Quantos produtos custam mais de R$ 1000.
# C) Qual é o nome do produto mais barato.

print('\033[1;31mSUPERMERCADO: ADICIONE ALGO AO CARRINHO DE COMPRAS!!!\033[m')

c = 0

contador = 0
preco = []
produto = []
total = 0
produto1000 = []
quantidade = []
quantidade1000 = 0
barato = float("INF")
precobarato = 0
produtobarato = float("INF")

while True:
    print(f'\033[1;34m{c+1}º PRODUTO\033[m')
    produto.append(input(f'Digite o nome do {c+1}º produto: ').strip().lower())
    preco.append(input(f'Digite o preço do {c+1}º produto: R$ ').strip())
    for i in range(0, len(preco[c])):
        if not preco[c][i].isnumeric():
            contador += 1
        if preco[c][i] == '.':
            contador -= 1
    while contador != 0:
        contador = 0
        print('\033[1;31mDIGITE UM PREÇO VÁLIDO. (R$ 200; R$ 200.50; R$ 1200.50...)\033[m')
        del preco[c]
        preco.append(input(f'Digite o preço do {c+1}º produto: R$ ').strip())
        for i in range(0, len(preco[c])):
            if not preco[c][i].isnumeric():
                contador += 1
            if preco[c][i] == '.':
                contador -= 1
    preco[c] = float(preco[c])
    quantidade.append(input(f'Digite a quantidade do {c+1}º produto a ser considerada: ').strip().lower())
    while not quantidade[c].isnumeric() or quantidade[c] == '0':
        print('\033[1;31mDIGITE UMA QUANTIDADE VÁLIDA!!!')
        del quantidade[c]
        quantidade.append(input(f'Digite a quantidade do {c+1}º produto a ser considerada: ').strip().lower())
    quantidade[c] = int(quantidade[c])
    total += (preco[c] * quantidade[c])
    if preco[c] > 1000:
        produto1000.append(produto[c])
        quantidade1000 += 1
    if preco[c] < barato:
        produtobarato = produto[c]
        precobarato = preco[c]
    c += 1
    print('\033[1;33m=-\033[m' * 60)
    resposta = input('Deseja adicionar mais produtos no carrinho de compras? (Sim ou Não): ').strip().lower()
    while resposta not in ['sim', 'nao', 'não']:
        print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA. SIM OU NÃO!!!\033[m')
        resposta = input('Deseja adicionar mais produtos no carro de compras? (Sim ou Não): ').strip().lower()
    print('\033[1;33m=-\033[m' * 60)
    if resposta in ['não', 'nao']:
        break
print('\033[1;34mVALOR DO CARRINHO DE COMPRAS\033[m')
print(f'O Valor total do carrinho de compras é de \033[1;32mR$ {total:.2f}.\033[m')
if quantidade1000 == 0:
    print('Nenhum produto do carrinho custa mais de R$ 1000,00.')
elif quantidade1000 == 1:
    print(f'{quantidade1000} Produto do carrinho custa mais de R$ 1000,00. \033[1;31m{produto1000}\033[m')
elif quantidade1000 > 1:
    print(f'{quantidade1000} Produtos do carrinho custam mais de R$ 1000,00. \033[1;31m{produto1000}\033[m')
print(f'O produto mais barato é o(a) \033[1;32m{produtobarato}.\033[m e custa \033[1;32m{precobarato}\033[m')

print('\033[1;33m=-\033[m' * 60)

print('\033[1;34mFORMA DE PAGAMENTO\033[m')

while True:
    pagamento = input('OPÇÕES DE PAGAMENTO:\n\033[1;31m[1]\033[m - À Vista no dinheiro ou cheque.\n\033[1;31m[2]\033[m - À Vista no cartão.\n\033[1;31m[3]\033[m - Em até 2x no cartão.\n\033[1;31m[4]\033[m - 3x ou mais no cartão.\nEscolha a condição de pagamento para este produto: ')
    while pagamento not in ['1', '2', '3', '4']:
        print('\033[1;31mDIGITE UMA FORMA DE PAGAMENTO VÁLIDA!!!\033[m')
        pagamento = input('OPÇÕES DE PAGAMENTO:\n\033[1;31m[1]\033[m - À Vista no dinheiro ou cheque.\n\033[1;31m[2]\033[m - À Vista no cartão.\n\033[1;31m[3]\033[m - Em até 2x no cartão.\n\033[1;31m[4]\033[m - 3x ou mais no cartão.\nEscolha a condição de pagamento para este produto: ')

    print('\033[1;33m=-\033[m' * 60)
    print('\033[1;34mPAGAMENTO\033[m')

    if pagamento == '1':
        valor = total * 0.9
        print(f'Para pagamento à vista no dinheiro ou cheque você receberá 10% de desconto. Portanto, o valor a ser pago nesta compra será de \033[1;32mR$ {valor:.2f}.\033[m')
    elif pagamento == '2':
        valor = total * 0.95
        print(f'Para pagamento à vista no cartão você receberá 5% de desconto. Portanto, o valor a ser pago nesta compra será de \033[1;32mR$ {valor:.2f}.\033[m')
    elif pagamento == '3':
        valor = total
        print(f'Para pagamento no cartão em 2x você não recebe desconto. Assim, o valor a ser pago nesta compra será de R$ {valor:.2f} com 02 parcelas de R$ {valor/2:.2f}.')
    elif pagamento == '4':
        valor = total * 1.20
        parcelas = input('Digite em quantas vezes (entre 3 e 12 vezes) você deseja parcelar: ').strip()
        while parcelas not in ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
            print('\033[1;31mDIGITE UMA OPÇÃO VÁLIDA DE PARCELAMENTO!!!\033[m')
            parcelas = input('Digite em quantas vezes (entre 3 e 12 vezes) você deseja parcelar: ').strip()
        parcelas = int(parcelas)
        print(f'Para pagamento no cartão de 3x ou mais você terá que pagar um juros de 20%. Logo, o valor total a ser pago nesta compra será de \033[1;31mR$ {valor:.2f}\033[m e o parcelamento foi escolhido com {parcelas} parcelas de \033[1;31mR$ {valor/parcelas:.2f}\033[m')
    print('\033[1;33m=-\033[m' * 60)
    resposta = input('Deseja verificar outra opção de pagamento? (Sim ou Não): ')
    print('\033[1;33m=-\033[m' * 60)
    if resposta in ['nao', 'não']:
        print('\033[1;31mFIM DE COMPRAS\033[m')
        break
