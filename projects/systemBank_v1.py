'''
Projeto: Sistema Bancário - Versão 1.0
Objetivos: Criar uma extrutura simples de depósito, saque, extratos.

Regras do sistema:

- OPERAÇÃO DE DEPÓSITO
- Apenas será permitido realizar depósitos de valores positivos
- Todos os depósitos armazenados em uma variável e exibidos na operação de extrato

- OPERAÇÃO DE SAQUE
- O limite diário são de apenas 3 saques
- O valor máximo de cada saque é R$ 500,00 por saque
- Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato

- OPERAÇÃO DE SALDO
- Caso não haja saldo, exibir uma mensagem informando que não é possível realizar o saque

- OPERAÇÃO DE EXTRATO
- Listar todos os depósitos e saques realizados na conta
- Listar no final o saldo atual da conta no formato R$ xxxx.xx 
'''

# Tela do sistema
menu = """

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

Digite a opção desejada: 
"""

# Declaração de variáveis e constantes
saldo = 0
extrato = 0
numero_saques = 0
LIMITE = 500
LIMITE_SAQUES = 3

# Execução
while True:

    opcao = input(menu.lower()) # converte para minúsculas

    if opcao == 'd':
        valor = float(input('Informe o valor para depósito: '))

        if valor < 0:
            print('Valor de depósito inválido')
         
        else:
            saldo += valor
            extrato += valor

            print(f'Depósito no valor de R$ {valor:.2f} realizado com sucesso')

    elif opcao == 's':
        valor = float(input('Informe o valor a ser sacado: '))

        excedeu_saldo = valor > saldo   # Verifica se o valor do saque é maior que o saldo
        excedeu_limite = valor > LIMITE # Verifica se o valor do saque é maior que o limite permitido
        excedeu_saques = numero_saques >= LIMITE_SAQUES # Verifica se o número de saques diários excedeu o limite definido
        
        if excedeu_limite:
            print('Valor de limite de saque acima do permitido.')
                       
        elif excedeu_saldo:
            print('Valor de saque maior que saldo disponível. Saque não realizado.')
            
        elif excedeu_saques:
            print('Número de saques diários excedidos. Saque não realizado.')

        elif valor > 0:
            saldo -= valor       # Atualiza o Saldo
            extrato += valor     # Atualiza o Extrato
            numero_saques += 1   # Incrementa o número de saques realizados

            print(f'Saque no valor de {valor:.2f} realizado com sucesso. Seu saldo atual é: {saldo:.2f}')
            print(f'Total de saques realizados no dia: {numero_saques}. Total permitido por dia: {LIMITE_SAQUES}')
        
        else:
             print('Valor de saque inválido, operação não realizada.')

    elif opcao == 'e':
        print(f'Seu saldo atual em conta é: {saldo:.2f}')
        print(f'Valor do último saque foi: {valor:.2f}')
       
    elif opcao == 'q':
        print('Saindo do sistema.')
        break

    else:
        print('Operação inválida, or favor selecione novamente operação desejada.')

    