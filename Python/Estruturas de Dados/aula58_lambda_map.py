lista1 = [1,2,3,4]

#def multi(x):
#    return x * 2

#lista2 = map(lambda x: x * 2, lista1) Desta forma tambem funciona 

print(list(map(lambda x: x * 2, lista1))) # Uma forma pequena e com a mesma função

# Coloca a função lambda na lista1, depois voce mapea ela e por final transforma em lista