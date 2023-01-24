a = int(input('Digite um número para soma: '))
b = int(input('Digite outro número para soma: '))

def soma(a,b):
    c = a + b
    print(f'O resultado entre {a} e {b} é {c}') # Esse print não é uma variável global, pertence somente a função

soma(a,b)

# Usei o método de argumento neste código, usando na função soma(a,b) para poder aparecer ma print formatada 'f'