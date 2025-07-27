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

for linha in matriz: # a,3,5 (resultados da coluna de índice 1)
    print(linha[1])


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
    quadrado.append(numero * 2)
    print(quadrado)


# Modificando valores - Usando LIST COMPREHAND
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)
