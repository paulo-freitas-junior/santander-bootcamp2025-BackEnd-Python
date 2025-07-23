# Conversão de tipos de variáveis
# Em Python, podemos converter tipos de dados usando funções integradas.

# As funções mais comuns para conversão são:

# int() - Converte para inteiro
# float() - Converte para ponto flutuante
# str() - Converte para string
# bool() - Converte para booleano
# complex() - Converte para número complexo


# Convertendo uma string para inteiro
preco = 10
print(f'Preço original: {preco} ({type(preco)})')

# Convertendo para float
preco_float = float(preco)
print(f'Preço convertido para float: {preco_float} ({type(preco_float)})')

# Convertendo para inteiro
preco_int = int(preco_float)
print(f'Preço convertido para int: {preco_int} ({type(preco_int)})')

# Convertendo para booleano
preco_bool = bool(preco_int)
print(f'Preço convertido para booleano: {preco_bool} ({type(preco_bool)})')

# Convertendo para string
preco_str = str(preco)
print(f'Preço convertido para string: {preco_str} ({type(preco_str)})')

# Convertendo para complexo
preco_complexo = complex(preco)
print(f'Preço convertido para complexo: {preco_complexo} ({type(preco_complexo)})')

# Convertendo uma string para inteiro
preco_str = "10"
preco_int = int(preco_str)
print(f'Preço convertido de string para int: {preco_int} ({type(preco_int)})')

# Convertendo uma string para float
preco_float = float(preco_str)
print(f'Preço convertido de string para float: {preco_float} ({type(preco_float)})')

# Convertendo uma string para booleano
preco_bool = bool(preco_str)
print(f'Preço convertido de string para booleano: {preco_bool} ({type(preco_bool)})')

# Convertendo uma string para complexo
preco_complexo = complex(preco_str)
print(f'Preço convertido de string para complexo: {preco_complexo} ({type(preco_complexo)})')

# Convertendo um booleano para inteiro
preco_bool = True
preco_int = int(preco_bool)
print(f'Preço convertido de booleano para int: {preco_int} ({type(preco_int)})')

# Convertendo um booleano para float
preco_float = float(preco_bool)
print(f'Preço convertido de booleano para float: {preco_float} ({type(preco_float)})')

# Convertendo um booleano para string
preco_str = str(preco_bool)
print(f'Preço convertido de booleano para string: {preco_str} ({type(preco_str)})')

# Convertendo um booleano para complexo
preco_complexo = complex(preco_bool)
print(f'Preço convertido de booleano para complexo: {preco_complexo} ({type(preco_complexo)})')

# Convertendo um complexo para inteiro
preco_complexo = 10 + 5j
preco_int = int(preco_complexo.real)  # Apenas a parte real é convertida
print(f'Preço convertido de complexo para int: {preco_int} ({type(preco_int)})')

# Convertendo um complexo para float
preco_float = float(preco_complexo.real)  # Apenas a parte real é convertida
print(f'Preço convertido de complexo para float: {preco_float} ({type(preco_float)})')

# Convertendo um complexo para string
preco_str = str(preco_complexo)
print(f'Preço convertido de complexo para string: {preco_str} ({type(preco_str)})')

# Convertendo um complexo para booleano
preco_bool = bool(preco_complexo)
print(f'Preço convertido de complexo para booleano: {preco_bool} ({type(preco_bool)})')