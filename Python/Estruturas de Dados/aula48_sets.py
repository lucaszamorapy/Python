# Sets evita itens duplicados
# Não utiliza index

list1 = [10,20,30,40,50]
list2 = [10,20,60,70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) #Union = vai unir as duas listas, porem se tiver numeros iguais ele nao vai repetir
print(num1 - num2) #Difference = pegar as diferenças entre as duas listas
print(num1 ^ num2) #Symmetric Difference = ele retira os itens duplicados nas listas
print(num1 & num2) #And = pega os itens duplicados nas duas listas