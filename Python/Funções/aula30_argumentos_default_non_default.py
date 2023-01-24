def boas_vindas(nome, quantidade=6):
    print(f'Olá {nome}!')
    print(f'Temos {quantidade} laptops disponíveis')


boas_vindas('Lucas')

# Non-Default =  aquele que voce nao define o valor no parametro, por exemplo no parametro 'nome' nao tem nada dentro
# Default = aquele que voce define o valor no parametro, por exemplo no parametro 'quantidade' tem o valor 6 dentro
# Obs = non-default sempre tem que esta em primeiro e depois vir o default, isso é uma regra do python