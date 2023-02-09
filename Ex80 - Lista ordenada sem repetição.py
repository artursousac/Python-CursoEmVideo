# Exercício 80. Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

print('\033[1;31mENTRADAS DO USUÁRIO\033[m')

valores = []
c = 0

while True:
    valor = input('Digite um valor numérico: ').strip()
    while not valor.isnumeric():
        print('\033[1;31mDIGITE UM NÚMERO VÁLIDO MAIOR OU IGUAL A 0!!!\033[m')
        valor = input('Digite um valor numérico: ').strip()
    valor = int(valor)
    if c in [0, 1]:
        valores.append(valor)
        resposta = input('\033[1;34mDeseja digitar mais números? (Sim ou Não): \033[m').strip().lower()
        if c in [1]:
            if valores[0] > valores[1]:
                valores[0], valores[1] = valores[1], valores[0] # Ou utilizar valores[1] = valores[0] e depois valores[0] = valor
        while resposta not in ['sim', 'não', 'nao', 's', 'n']:
            print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA!!!\033[m')
            resposta = input('\033[1;34mDeseja digitar mais números? (Sim ou Não): \033[m').strip().lower()
        if resposta in ['não', 'nao', 'n']:
            break
    elif c > 1:
        for d in range(0, len(valores)):
            if valor <= valores[d]:
                valores.insert(d, valor)
                break
            elif valor >= valores[len(valores)-1]:
                valores.insert(len(valores)+1, valor)
                break
        resposta = input('\033[1;34mDeseja digitar mais números? (Sim ou Não): \033[m').strip().lower()
        while resposta not in ['sim', 'não', 'nao', 's', 'n']:
            print('\033[1;31mDIGITE UMA RESPOSTA VÁLIDA!!!\033[m')
            resposta = input('\033[1;34mDeseja digitar mais números? (Sim ou Não): \033[m').strip().lower()
        if resposta in ['não', 'nao', 'n']:
            break
    c += 1

print('\033[1;33m=-\033[m' * 60)
print('\033[1;31mRESPOSTA DO PROGRAMA\033[m')

print(f'Os valores digitados, em ordem crescente, são: {valores}')
