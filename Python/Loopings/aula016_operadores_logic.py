# Usando o and

'''renda_acima_5mil = True
nome_limpo = True

if renda_acima_5mil and nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamento Negado')'''

# Usando o or

renda_acima_5mil = False
nome_limpo = True

if renda_acima_5mil or nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamento Negado')

# O operador lógico or sempre vai ser True mesmo se tiver um False