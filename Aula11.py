# Aula 11 - Cores no Terminal

"""
Existem alguns estilos, sendo 0 = padrão; 1 = Bold (negrito); 4 = Underline (sublinhado); 7 = Negativo (inversão, ou seja, para gerar letra preta é utilizar ele)
Existem algumas cores de texto. 30 Branco, 31 Vermelho, 32 Verde, 33 Amarelo, 34 Azul, 35 Roxo, 36 Azul Claro, 37 Cinza
Existem, também, as cores de back, ou de fundo, que começam a partir do 40 e seguem a mesma sequência do anterior.
A formatação é dada por \033[4:33:44m, ou seja, [Estilo: Cor do texto: Cor de Fundo
o \033 é o que funciona melhor em Python e sempre termina com "m".
Se utilizarmos somente \033[m, ele vai limpar e voltar ao padrão.
Quando utilizamos o comando, ele inicia e vai manter essa mesma estrutura durante toda a frase, até ser alterada novamente. Por exemplo: \033[4:34m {nome} \033[m
É possível criar um dicionário, como por exemplo. cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':\033[7;30m'}

"""

nome = 'Artur'
print(f'\033[1;36mOlá {nome}, \033[1;32mtudo bem?')