set1 = {'a', 'b', 'c'}
set2 = {'a', 'b', 'e'}
set3 = {'c', 'd', 'f'}

#set4 = set1.union(set2) vai unir as duas listas, porem se tiver numeros iguais ele nao vai repetir
#set4 = set1.difference(set3) pegar as diferenças entre as duas listas
set4 = set1.intersection(set2) #vai pegar o que tem de igual nos dois
#set4 = set1.symmetric_difference(set3) # retira os dois C que aparecem iguais nas duas listas
print(set4)