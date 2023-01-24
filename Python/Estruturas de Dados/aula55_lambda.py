# É uma função (pequena) sem nome
# Pode ter vários argumentos mas somente uma expressão
# Muito utilizado dentro de outras funções
# Código mais 'clean'
# lambda tem que colocar as variaveis quando imprimir, já na função não precisa

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

soma = lambda n1,n2: n1 + n2

print(soma(n1,n2))