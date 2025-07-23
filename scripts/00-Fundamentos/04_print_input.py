# Funções de entrada e saída
# Em Python, usamos a função input() para ler dados do usuário e a função print() para exibir dados na tela.

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

# Função de saída
print(f'Olá, {nome}! Você tem {idade} anos.')
print(nome, idade)                  # Imprime os valores separados por espaço
print(nome, idade, end="...\n")     # Imprime os valores separados por espaço e adiciona uma nova linha no final
print(nome, idade, sep="*")         # Imprime os valores separados por asterisco

