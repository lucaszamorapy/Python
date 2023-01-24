# Criar uma promoção de um produto no valor de R$100.
# While bastante usado para condiçao de um looping

valor = 100
dia = 0
while valor >= 20: # Enquanto o valor for maior ou igual a 20
    dia += 1 # Adicionar +1 na variavel dia que esta valendo 0
    print('No dia {} o produto vai ser vendido por R${},00'.format(dia,valor))
    valor -=5 # Subtrair -5 na variavel valor que esta valendo 100