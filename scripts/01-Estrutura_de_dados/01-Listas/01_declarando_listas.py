# EXEMPLOS DE LISTAS EM PYTHON
# Armazena de maneira sequencial qualquer tipo de objeto.
# Usando o construtor "list" ou declarando direto na variável.
#=================================

frutas =['laranja', 'maçã', 'uva', 'pera']

print(frutas)
print(frutas[1]) # maçã
print(frutas[3]) # pera

# valores negativos
print(frutas[-1]) # pera
print(frutas[-4]) # laranja

frutas = [] # declaração de uma lista vazia
print(frutas)

letras = list('Python') # cada letra será um objeto específico (string é um elemento interável)
print(letras)

numeros = list(range(10)) # valores de 0-9
print(numeros)

carro = ['Ferrari', 'F8', 4200000, 2020, 2900, 'São Paulo', True] # lista de atributos
print(carro)


# EXEMPLO DE LISTAS EM UMA MATRIZ BIDIMENSIONAL (LISTAS ANINHADAS)
# Linhas e Colunas [linha][coluna]
# Linhas e Colunas indexadas à partir de 0
#================================================================

matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

print(matriz[0]) # [1, 'a', 2]
print(matriz[0][0]) # 1
print(matriz[1][2]) # 4
print(matriz[0][-1]) # 2
print(matriz[-1][-1]) # c

for coluna in matriz: # a,3,5 (resultados da coluna de índice 1)
    print(coluna[1])


# FATIAMENTO (SLICING)
# lista[inicio:fim:passo]
# Inicio : índice onde o corte começa (inclusivo)
# Fim: índice onde  corte termina (exclusívo)
# Passo: de quantos em quantos elementos quer pular (opcional)
#================================================================

lista = ['P','Y','T','H','O','N']

print(lista[2:]) # ['T','H','O','N']
print(lista[:2]) # ['P','Y']
print(lista[1:3]) # ['Y','T']
print(lista[0:3:2]) # ['P','T']
print(lista[0:5:3]) # ['P','H']
print(lista[::]) # ['P','Y','T','H','O','N']
print(lista[::-1]) # ['N','O','H','T','Y','P']

# Percorrendo os dados de uma lista - FOR
carros =['gol','celta','palio']

for carro in carros:
    print(carro)

# ENUMERATE - saber qual índice do objeto na lista
carros =['opala','omega','veraneio']

for indice, carro in enumerate(carros):
    print(f'{indice}:{carro}')


# LIST COMPRESSION - compressão de lista
# criar uma lista com base ns valores de uma lista existente (filtro)
# gerar uma nova lista aplicando alguma modificação nos elementos lista existente

# Filtro 1 - Usando FOR
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        print(pares)


# Filtro 2 - Usando LIST COMPRESSION
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)


# Modificando valores - Usando FOR
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
    print(quadrado)


# Modificando valores - Usando LIST COMPREHAND
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)


# MÉTODOS DA CLASSE LIST
#===================================================

# [].append - Inserir objetos dentro da lista
# ----------------------------------------------
lista = []

lista.append(1)
lista.append('Python')
lista.append([40, 30, 20])

print(lista)


# [].clear - Limpar objetos dentro da lista
# ---------------------------------------------
lista = [1, 'Python', [40, 30, 20]]
print(lista)

lista.clear()
print(lista)


# [].copy - Gera uma cópia dos objetos existentes na lista
# ---------------------------------------------------------
lista = [1, 'Python', [40, 30 ,20]]

lista2 = lista.copy()

print(f'Conteúdo da lista: {lista}')
print(f'Conteúdo da lista 2: {lista2}')
print(f'Identificador da lista: ' + (str(id(lista))))
print(f'Identificador da lista2: ' + (str(id(lista2))))


# [].count - Conta número de vezes que um objeto aparece na lista
# ---------------------------------------------------------------
cores = ['vermelho','azul','verde','azul','amarelo']

print(f'Vermelho aparece: {cores.count('vermelho')} vez(es) na lista')
print(f'Azul aparece: {cores.count('azul')} vez(es) na lista')
print(f'Verde aparece: {cores.count('verde')} vez(es) na lista')
print(f'Amarelo aparece: {cores.count('amarelo')} vez(es) na lista')


# [].extend - Adicionar elementos de OUTRA LISTA em uma lista existente
# ---------------------------------------------------------------------
linguagens = ['Python','Js','C']
print(f'Lista das primeiras linguagens: {linguagens}')

linguagens.extend(['Java','CSharp'])
print(f'Lista atualizada das linguagens: {linguagens}')

linguagens2 = ['SQL','R','Julia']
linguagens.extend(linguagens2) # Adicionando nova lista na listagem 1
print(f'Listas de linguagens1 + Linguagens2: {linguagens}')


# [].index - Qual ocorrência de índice de determinado objeto
# ----------------------------------------------------------

linguagens =['Python','Js','C','Java','CSharp']
print(f'Índice do objeto Python na lista é: {linguagens.index('Python')}')
print(f'Índice do objeto Js na lista é: {linguagens.index('Js')}')
print(f'Índice do objeto C na lista é: {linguagens.index('C')}')
print(f'Índice do objeto Java na lista é: {linguagens.index('Java')}')
print(f'Índice do objeto CSharp na lista é: {linguagens.index('CSharp')}')


# [].pop - Remover objetos de uma lista à partir do último elemento ADICIONADO!
# -----------------------------------------------------------------------------

linguagens = ['Python','Js','C','Java','Csharp']
print(f'Removendo Csharp da lista de linguagens: {linguagens.pop()}')
print(f'Removendo Java da lista de linguagens: {linguagens.pop()}')
print(f'Removendo Python da lista de linguagens usando índice: {linguagens.pop(0)}')


# [].remove - Remove objetos específicos de uma lista
# ---------------------------------------------------

linguagens = ['Python','Js','C','Java','Csharp']
print('Removendo a linguagem C da lista: ' + str(linguagens.remove('C')))
print(f'Removendo a linguagem Java da lista: {linguagens.remove('Java')}')
print(f'Linguagens restantes na lista: {linguagens}')


# [].reverse - Realiza o espelhamento inverso dos objetos na lista
# -----------------------------------------------------------------

linguagens = ['Python','Js','C','Java','Csharp']
linguagens.reverse()
print(f'Lista de linguagens em ordem invertida: ' + str(linguagens))


# [].sort - Ordenação dos objetos dentro da lista
# -----------------------------------------------

linguagens = ['Python','Js','C','Java','Csharp']
linguagens.sort() # ordenação alfabética
print(linguagens)

linguagens = ['Python','Js','C','Java','Csharp']
linguagens.sort(reverse=True) # ordenação alfabética invertida
print(linguagens)

linguagens = ['Python','Js','C','Java','Csharp']
linguagens.sort(key=lambda x: len(x)) # ordenação por tamanho de objeto (menor para maior)
print(linguagens)

linguagens = ['Python','Js','C','Java','Csharp']
linguagens.sort(key=lambda x: len(x), reverse=True) # ordenação por tamanho de objeto (maior para menor)
print(linguagens)


# [].len - Verifica o tamanho dos objetos dentro de uma lista
# -----------------------------------------------------------

linguagens = ['Python','Js','C','Java','Csharp']
print(f' Existem {len(linguagens)} objetos dentro da lista de linguagens')


# [].sorted - Ordenação de Interáveis em uma lista
# ------------------------------------------------

linguagens = ['Python','Js','C','Java','Csharp']
print(sorted(linguagens, key=lambda x: len(x)))

linguagens = ['Python','Js','C','Java','Csharp']
print(sorted(linguagens, key=lambda x: len(x), reverse=True))


