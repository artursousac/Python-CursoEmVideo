# Exercício 83. Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
# na ordem correta.

frase = input('Digite uma expressão separada corretamente por parênteses: ').strip().lower()

contador = 0

for c in range(0, len(frase)):
    if frase[c] == '(':
        contador += 1
    elif frase[c] == ')':
        contador -= 1

if contador == 0:
    print('Expressão correta!')
else:
    print('Expressão incorreta!')
