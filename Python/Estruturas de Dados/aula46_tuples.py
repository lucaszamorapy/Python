# Tuples tem a mesma função que listas porém voce nao consegue alterar nem remover nada de dentro do tuple
# São uteis em caso que voce nao va alterar sua lista, pois tuples consumem menos espaço de memoria


carros_list = ['Gol', 'Golf', 'Jetta', 'Polo']
carros_tuple = ('Gol', 'Golf', 'Jetta', 'Polo')

carros_list.append('Fox')
carros_tuple.append('Fox')

print(carros_list)
print(carros_tuple)

