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
