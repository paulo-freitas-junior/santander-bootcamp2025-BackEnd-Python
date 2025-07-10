# Tipos de operadores em Python
# Em Python, os operadores são usados para realizar operações em variáveis e valores.

# Os principais tipos de operadores em Python são:
# 1. Operadores Aritméticos: Usados para realizar operações matemáticas.
# 2. Operadores de Comparação: Usados para comparar valores.
# 3. Operadores Lógicos: Usados para realizar operações lógicas.
# 4. Operadores de Atribuição: Usados para atribuir valores a variáveis.
# 5. Operadores Bitwise: Usados para realizar operações bit a bit.
# 6. Operadores de Identidade: Usados para verificar se dois objetos são o mesmo objeto.
# 7. Operadores de Membro: Usados para verificar se um valor está presente em uma sequência (como listas, tuplas, etc.).

# 1. Operadores Aritméticos
# Operadores aritméticos são usados para realizar operações matemáticas básicas.
print("Operadores Aritméticos:")
print("Adição:", 10 + 5)                # Soma
print("Subtração:", 10 - 5)             # Subtração
print("Multiplicação:", 10 * 5)         # Multiplicação
print("Divisão:", 10 / 5)               # Divisão
print("Divisão inteira:", 10 // 3)      # Divisão inteira
print("Módulo:", 10 % 3)                # Módulo (resto da divisão)
print("Exponenciação:", 10 ** 2)        # Exponenciação

# 2. Operadores de Comparação
# Operadores de comparação são usados para comparar valores e retornam um valor booleano (True ou False).
print("\n")                             # Linha em branco para melhor legibilidade
print("Operadores de Comparação:")
print("Igual a:", 10 == 10)             # Igualdade
print("Diferente de:", 10 != 5)         # Diferença
print("Maior que:", 10 > 5)             # Maior que

# 3. Operadores de atribuição
# Operadores de atribuição são usados para atribuir valores a variáveis.
print("\n")                                 # Linha em branco para melhor legibilidade
print("Operadores de Atribuição:")
x = 10
print("Atribuição:", x)                     # Atribuição simples
x += 5
print("Atribuição com adição:", x)          # Atribuição com adição
x -= 3
print("Atribuição com subtração:", x)       # Atribuição com subtração
x *= 2
print("Atribuição com multiplicação:", x)   # Atribuição com multiplicação
x /= 2
print("Atribuição com divisão:", x)         # Atribuição com divisão

# 4. Operadores Lógicos
print("\n")                                 # Linha em branco para melhor legibilidade
print("Operadores Lógicos:")
print("E:", True and False)                 # E lógico
print("OU:", True or False)                 # OU lógico
print("NÃO:", not True)                     # NÃO lógico

saldo = 1000
saque = 200
limite = 100
conta_especial = True
print(f'Verificando se existe saldo: {saldo >= saque and saque <= limite}')  # Verifica se o saldo é suficiente para o sque e se o saque está dentro do limite
print(f'Verificando se o saldo é maior ou igual ao saque ou saque é menor ou igual ao limite: {saldo >= saque or saque <= limite}') # Verifica se  saldo é maior ou igual ao saque u se o saque é menor ou igual ao limite

print(f'{(saldo >=saque and saque <= limite) or (conta_especial and saldo >= saque)}')

conta_normal_com_saldo_suficiente =(saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)
verifica_saque = (conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente)
print(f'Verificando se o saque pode ser realizado: {verifica_saque}')

# 5. Operadores de Identidade
# Operadores de identidade são usados para verificar se dois objetos são o mesmo objeto.
print("\n")
print("Operadores de Identidade:")
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200
print('É o mesmo objeto?', curso is nome_curso)  # Verifica se curso e nome_curso são o mesmo objeto
print('É diferente o objeto?', curso is not nome_curso)
print('Saldo é igual ao limite?', saldo is limite)

# Operadores de Associação
# Operadores de associação são usados para verificar se um valor está presente em uma sequência (como listas, tuplas, etc.).
print('\n')
curso  = "Curso de Python"
frutas = ['laranja', 'uva', 'limão'] # Lista de strings
saques = [1500, 100]
print('A palavra "Python" está no curso?', 'Python' in curso)  # Verifica se 'Python' está em curso
print('A fruta "maçã" NÃO está na lista de frutas?', 'maçã' not in frutas) # Verifica se 'maça' não está na lista de frutas
print('O valor 200 está na lista de saques?', 200 in saques) # Verifica se 200 está na lista de saques

