# Desafios de Código - Explorando Operadores e Manipulação de Strings

# Dicionário com os valores de desconto
#===================================================================================
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:
if cupom in descontos:
    desconto = descontos[cupom]
    preco_final = preco * (1 - desconto)
    print(f'{preco_final:.2f}')
else:
    print('Cupom inválido.')



# Validador de formato de e-mails contendo '@' e domínio 'gmail.com' e 'outlook.com'
#===================================================================================

# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:

""" Regras para um e-mail válido:

- Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
- Não pode começar ou terminar com "@".
- Não pode conter espaços.

"""

def validador_email(email):
    if not email or email.startswith('@') or email.endswith('@') or ' ' in email:
        return False
    return '@' in email and (email.endswith('gmail.com') or email.endswith('outlook.com'))

if validador_email(email):
  print('E-mail válido')
else:
  print('E-mail inválido')

