# Exercício 01 #

print('\033[1;33m===== DESAFIO 01 =====\033[m')

cont = 0

nome = input('Qual é o seu nome? ').strip() #Aqui vamos ler o nome que o usuário digitar e adicionar na variável "nome"
for c in range(0,len(nome)): #Este comando for foi criado para verificar se alguma posição do nome digitado possui algo não alfabético (como números ou caracteres especiais !*&...)
    if not nome[c].isalpha(): #Caso tenha algo não alfabético, estou utilizando a variável "cont" para receber um valor.
        cont += 1
        if nome[c] == ' ': #Como sabemos que o usuário pode digitar espaço para escrever o seu nome e sobrenome, criei um if para, caso seja digitado o espaço, retirar o valor adicionado no "cont".
            cont -= 1
while cont > 0: #Ou seja, uso o comando while para verificar se o "cont" está maior que 0, pois, se estiver, significa que tem alguma palavra não alfabética no nome digitado.
    print('\033[1;31mDIGITE UM NOME VÁLIDO!!!\033[m') #Utilizo o print com essa mensagem em vermelho e com formato diferente para chamar atenção do usuário que precisa ser digitado um nome válido.
    nome = input('Qual é o seu nome? ').strip() #Caso o "cont" esteja maior que 0, ele irá entrar no while e solicitar um novo input pelo usuário.
    cont = 0 #Estou zerando o "cont" para realizar um novo for com o mesmo principio anterior.
    for c in range(0, len(nome)):
        if not nome[c].isalpha():
            cont += 1
            if nome[c] == ' ':
                cont -= 1
print(f'Olá, {nome}, prazer em te conhecer!') #Após o processo acima ocorrer, o programa só irá encerrar quando tiver sido digitado um nome real com palavras alfabéticas e irá mostrar na tela o resultado.
