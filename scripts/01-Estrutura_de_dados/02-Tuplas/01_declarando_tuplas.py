# DECLARANDO TUPLAS EM PYTHON
# Tuplas são imutáveis.

# Declarando as Tuplas
#=====================
frutas = ('laranja','pera','uva',)  # atenção ao uso da vírgula no final
letras = ('Python')
numeros = ([1,2,3,4])   # Tupla contendo um objeto de lista
pais = ('Brasil',)  #atenção ao uso da vírgula no final

# Acessando os valores das Tuplas
#================================
print(pais)
print(frutas[0])
print(frutas[1])
print(frutas[-3])

print(numeros[0])   # 1
print(numeros[2])   # 3


# EXEMPLO DE TUPLAS EM UMA MATRIZ BIDIMENSIONAL (LISTAS ANINHADAS)
# Linhas e Colunas [linha][coluna]
# Linhas e Colunas indexadas à partir de 0
#================================================================

matriz = (
    (1,'a',2),
    ('b',3,4),
    (5,6,'c'),
)

print(matriz)
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])


# FATIAMENTO (SLICING)
# lista[inicio:fim:passo]
# Inicio : índice onde o corte começa (inclusivo)
# Fim: índice onde  corte termina (exclusívo)
# Passo: de quantos em quantos elementos quer pular (opcional)
#================================================================

tupla = ('p','y','t','h','o','n',)

print(tupla[2:])    # ('t','h','o','n')
print(tupla[:2])    # ('p','y')
print(tupla[1:3])   # ('y','t')
print(tupla[0:3:2]) # ('p','t')
print(tupla[::])    # ('p','y','t','h','o','n')
print(tupla[::-1])  # ('n','o','h','y','y','p')


# MÉTODOS DA CLASSE TUPLE
#===================================================


# COUNT - contagem de objetos dentro da Tupla
#--------------------------------------------
cores =('vermelho','azul','verde','azul')

print(cores.count('vermelho'))  # 1
print(cores.count('azul'))  # 2
print(cores.count('verde')) # 1

# INDEX - identificar qual o índice do objeto dentro da tupla
#------------------------------------------------------------

linguagens = ('Python','Java','C','Js','R','Julia')

print(linguagens.index('R')) # 4
print(len(linguagens))  # 6