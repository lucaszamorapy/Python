# Array = matriz, similar a listas porem com melhor perfomance em caso a lista for muito grande
from array import array

letras = ['a', 'b', 'c', 'd']
numeros_i = ['1','2','3','4']
numeros_f = ['1.2','1.3','1.4','1.5']

letras = array('u', ['a', 'b', 'c', 'd'])           # u = para listas que só tem strings
numeros_i = array('i', [ 1, 2, 3, 4])               # i = para listas que só tem inteiros
numeros_f = array('f', [ 1.2, 1.3, 1.4, 1.5])       # f = para listas que só tem float

print(letras)
print(numeros_i)
print(numeros_f)