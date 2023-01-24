def agencia(**carro):
    return carro

a = agencia(Marca = 'Volkswagen', Modelo = 'Golf GTI', Motor = 2.0)
b = agencia(Marca = 'Nissan', Modelo = 'Skyline R34', Motor = 2.0)
c = agencia(Marca = 'Peugeot', Modelo = '207', Motor = 1.6)
d = agencia(Marca = 'Honda', Modelo = 'Civic Coupe 2002', Motor = 1.6)
print(a)
print(b)
print(c)
print(d)

''' Nomear os parametros faz com que voce nao precise mudar os parametros de cima, apenas colocando o **
'''