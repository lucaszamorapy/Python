from sys import getsizeof # Saber quanto de memória ta se alocada

# Generator Expression
# Uma forma mais rápida para listas, dicionário etc
# Menos memória alocada
# Valores
# Use quando for fazer list comprehsion com int
# Apenas tirar os [] e substituit por ()

number1 = [x / 2 for x in range(1, 7)]
print(type(number1)) # Type =  ver o tipo 
print(number1)
print(getsizeof(number1))       #Tamanho de espaço que esta sendo alocado

number2 = (x / 2 for x in range(1, 7))
print(type(number2))
print(list(number2))              #Sempre transformar em lista, atraves do list
print(getsizeof(number2))        #Tamanho de espaço que esta sendo alocado