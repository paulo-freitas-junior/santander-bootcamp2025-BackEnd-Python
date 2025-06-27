# Variáveis e Constantes

# Em Python, não há uma distinção formal entre variáveis e constantes como em outras linguagens.
# No entanto, por convenção, usamos letras maiúsculas para constantes e letras minúsculas para variáveis.
# Variáveis são usadas para armazenar dados que podem mudar durante a execução do programa.
# Constantes são usadas para armazenar dados que não devem mudar.

# Variáveis
idade = 48
nome = 'Paulo'
altura = 1.75
print(f'{nome} tem {idade} anos e {altura} metros de altura.')

# Constantes
PI = 3.14159
NOME_COMPLETO = 'Paulo Roberto'
print(f'O valor de PI é {PI} e o nome completo é {NOME_COMPLETO}.')

DEBUG = True  # Usado para ativar ou desativar mensagens de depuração
ESTADOS = ['SP', 'RJ', 'MG', 'RS']  # Lista de estados brasileiros
print(f'Debug está {"ativado" if DEBUG else "desativado"} e os estados são: {", ".join(ESTADOS)}.')

# Caminho do projeto
# Em Python, podemos usar strings para representar caminhos de diretórios.
PATH = '/home/paulo/projetos/python'  
print(f'O caminho do projeto é {PATH}.')