# Métodos úteis da classe str
# Em Python, as strings são objetos da classe str e possuem diversos métodos úteis para manipulação

# Maísculas, minúsculas e título
#=================================================
curso = "pYtHon"
print(curso.upper()) # Converte para maiusculas
print(f'Palavra em maiúscula: {curso.upper()}')

print(curso.lower()) # Converte para minúsculas
print(f'Palavra em minúscula: {curso.lower()}')

print(curso.title()) # Converte para título
print(f'Palavra em título: {curso.title()}')


# Eliminação de espaços
#=================================================
curso = "   Python   "
print(curso.strip()) # Remove espaços no início e no final
print(f'Palavra sem espaços: {curso.strip()}')

print(curso.lstrip()) # Remove espaços no início (left)
print(f'Palavra sem espaços à esquerda: {curso.lstrip()}')

print(curso.rstrip()) # Remove espaços no final (right)
print(f'Palavra sem espaços à direita: {curso.rstrip()}')


# Junções e centralização
#=================================================
curso = "Python"
print(curso.center(10, '#')) # Centraliza a string em um campo de 10 caracteres, preenchendo com '#'
print(f'Palavra centralizada: {curso.center(10, '#')}')

print('.'.join(curso)) # Junta os caractares com '.'
print(f'Palavra com caracteres unidos por ponto: {'.'.join(curso)}')


# Interpolação de variáveis
#=================================================

nome ='Paulo'
idade = 48
profissao = 'Cientista de Dados'
linguagem ='Python'

# Old Style - Não é recomendado.
print('Nome: %s, Idade: %d, Profissão: %s, Linguagem: %s' % (nome, idade, profissao, linguagem))


# Método format - Recomendado porém não é melhor opção.
print('Nome: {}, Idade: {}, Profissão: {}, Linguagem: {}'.format(nome, idade, profissao, linguagem))
print('Nome: {name}, Idade: {age}, Profissão: {job}, Linguagem: {language}'.format(name=nome, age=idade, job=profissao, language=linguagem))

dados = {'name': nome, 'age': idade, 'job': profissao, 'language': linguagem}
print('Nome: {name}, Idade: {age}, Profissão: {job}, Linguagem: {language}'.format(**dados)) # Usando dicionário para formatar a string


# F-strings - Recomendado a partir do Python 3.6.
print(f'Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Linguagem: {linguagem}')

PI = 3.14159
print(f'Valor de PI: {PI:.2f}') # Formatação de número com duas casas decimais
print(f'Valor de PI: {PI:10.2f}') # Formatação de número com 10 caracteres, duas casas decimais


# Fatiamento de strings
# Fatiamento é uma técnica para acessar partes de uma string. (Start, Stop, Step)
#=================================================

nome = 'Paulo Roberto Freitas'
print(nome[0]) # Acessa o primeiro caractere = 'P'
print(nome[:5]) # Acessa do início até o índice 5 (não inclusivo) = 'Paulo'
print(nome[6:13]) # Acessa do índice 6 até o índice 13 (não inclusivo) = 'Roberto'
print(nome[14:]) # Acessa do índice 14 até o final = 'Freitas'
print(nome[0:5:2]) # Acessa do início até o índice 5 com passo 2 = 'Puo'
print(nome[:]) # Acessa toda a string = 'Paulo Roberto Freitas'
print(nome[::-1]) # Inverte a string


# Strings de múltiplas linhas
#=================================================
nome = 'Paulo'
mensagem = f"""
Olá meu nome é {nome}, e eu sou um desenvolvedor Python.
Estou aprendendo a manipular strings e fatiamento.
"""
print(mensagem)

# outro exemplo
print("""
=============== MENU ===============
1. Depositar
2. Sacar
3. Extrato
0. Sair
Escolha uma opção:
====================================
""")