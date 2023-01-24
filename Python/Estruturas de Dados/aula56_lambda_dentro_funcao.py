n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

def somar():
    resultado = lambda n1, n2: n1 + n2      # Pegando os argumentos n1 e n2 e somando eles
    return resultado(n1,n2) * 4             # Após somar, retornar o resultado armazenado multiplicando por 4

print(somar())



