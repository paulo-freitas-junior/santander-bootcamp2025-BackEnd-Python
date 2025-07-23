# Identação e Blocos
#===================

# Em Python, a indentação é usada para definir blocos de código.

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print('Valor sacado!')
        print('Saldo atual:', saldo - valor)

    print('Obrigado por ser nosso cliente!')

sacar(100) # Função para sacar dinheiro

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f'Valor depositado: {valor}')
    print('Saldo atual:', saldo)

depositar(200) # Função para depositar dinheiro


# Estruturas condicionais
#========================

# If
# -- Verifica se o saldo é maior ou igual ao saque
saldo = 2000
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print(f'Saque de {saque} realizado com sucesso!')

if saldo < saque:
    print(f'Saldo insuficiente para saque no valor de {saque}.')


# If/Else
# -- Verifica se o saldo é maior ou igual ao saque, caso contrário exime mensagem de saldo insuficiente
saldo = 2000
saque = float(input('Informe o valor do saque: '))

if saque <= saldo:
    print(f'Saque no valor de {saque} realizado com sucesso!')
else:
    print(f'Saldo insuficiente para saque no valor de {saque}. Saldo atual: {saldo}')


# Elif
# -- Estrutura condicional aninhada (if dentro de if)
saldo = 2000
opcao = int(input('Escolha uma opção:\n [1] Sacar \n [2] Extrato:'))

if opcao == 1:
    saque = float(input('Informe o valor do saque: '))
    if saque <= saldo:
        print(f'Saque no valor de {saque} realizado com sucesso!!')
elif opcao == 2:
    print(f'Seu saldo atual é: {saldo}')
else:
    print('Opção inválida!')

# Outro exemplo de estrutura condicional aninhada
conta_normal = True             # alterar entre True e False para testar
conta_universitaria = False     # alterar entre True e False para testar
saldo = 2000
saque = 500                     # alterar o valor do saque para testar
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print(f'Saque no valor de  {saque} realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print(f'Saque no valor de {saque} realizado com uso do cheque especial!')
    else:
        print('Saldo insuficiente para saque.')
elif conta_universitaria:
    if saldo >= saque:
        print(f'Saque no valor de {saque} realizado com sucesso!')
    else:
        print('Saldo insuficiente para saque.')
else:
    print('Sistema não reconhece seu tipo de conta, entrar em contato com o gerente!')


# If Ternário
# -- Ternário é uma forma compacta de escrever uma estrutura condicional simples
status = 'Sucesso' if saldo >= saque else 'Saldo insuficiente'
print(f'Status do saque: {status}')


# Estruturas de Repetição
#========================

a = int(input('Informe um número inteiro: '))
print(f'Você digitou {a}')
a += 1
print(f'Valor digitado + 1: {a}')
a += 1
print (f'Valor digitado + 2: {a}')


# For
# -- Estrutura de repetição que itera sobre uma sequência (como listas, tuplas, strings, etc.)
texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'                        # Constante
for letra in texto:
    if letra.upper() in VOGAIS:
        print(f'A letra digitada {letra} é uma vogal.')
    else:
        print(f'A letra digitada {letra} não é uma vogal.')
print()


# outro exemplo de for

texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'                        # Constante
for letra in texto:
    if letra.upper() in VOGAIS:         # Verifica se a letra é uma vogal
        print(letra, end=' ')           # Imprime as letras que são vogais
print()

# for usando a função range
# range(start, stop, step) -> range de números
# range(stop) -> range do object

list(range(4)) # Cria uma lista de números de 0 a 3

for numero in range(0,11):
    print(numero, end=' ') # Imprime números de 0 a 10

# exibindo a tabuada do 6
for numero in range(1, 11):
    print(f'6 x {numero} = {6 * numero}') # Imprime a tabuada do 6

# exibindo a tabuada do 6 com start, stop e step
for numero in range(0, 61, 6):
    print(numero, end=' ') # Imprime números de 0 a 60 com passo de 6


# While
# -- Estrutura de repetição que continua enquanto uma condição for verdadeira
opcao = -1
while opcao != 0:
    opcao = int(input('Informe uma opção: \n [1] Sacar \n [2] Extrato \n [0] Sair: '))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo o extrato...')
else:
    print('Obrigado por usar nosso sistema bancário.')


# Exemplo de while com break
while True:
    numero = int(input('Informe uma opção: \n [1] Sacar \n [2] Extrato \n [0] Sair: '))

    if numero == 0:
        print('Saindo do sistema.')
        break
    elif numero == 1:
        print('Sacando...')
    elif numero == 2:
        print('Exibindo o extrato...')
    else:
        print('Opção inválida. Digite uma opção válida!')

# Exemplo de while com continue ( continue sempre vem após o break )
while True:
    numero = int(input('Informe um número de 1 a 10 (0 para sair): '))

    if numero == 0:
        print('Saindo do sistema')
        break
    elif numero < 1 or numero > 10:
        print('Número inválido, tente novamente!')
        continue
    print(f'Você digitou o número {numero}.')

