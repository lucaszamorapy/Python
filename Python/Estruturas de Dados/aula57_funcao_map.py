# Muito utlizado em listas
# Aplicar uma função Iterable, por item. (list, tuple, dic etc.)

lista1 = [1,2,3,4]

def multi(x):
    return x * 2

lista2 = map(multi, lista1) # A variável x acabou sendo a lista1, e o resultado map vai ser armazenado na lista2

print(list(lista2))  # Transformando o map em lista com o list
