'''def soma():
    resultado = 0
    for num in range(1,6):                  # Usando in range
        resultado += num
    return resultado

x = soma()
print(x)'''

def mult(*numeros):     # Indica que dentro do parametro irá conter vários números
    resultado = 1       # Colocar o resultado valendo 1 foi uma boa ideia pois se iniciarmos com 0 a multiplicao iria zerar
    for num in numeros: # Pegando a variavel num e fazendo looping
        resultado *= num        # resultado = 0 x 2 (primeiro número)
    return f' a multiplicação dos números é {resultado}'


x = mult(2,3,4,7)
print(x)