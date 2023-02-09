# Exercício 04 - que leia algo pelo teclado e mostra na tela o tipo primitivo e todas as informações possíveis sobre ele

teste = input('Digite algo: ')
print(f'O "{teste}" é alfabético?', teste.isalpha())
print(f'O "{teste}" é númerico?', teste.isnumeric())
print(f'O "{teste}" é alfanumérico?', teste.isalnum())
