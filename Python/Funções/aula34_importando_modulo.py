import math    # Importando o modulo math para usar o fatorial na opção 5 

print('====== CALCULADORA MIL GRAU ======')
a = int(input('Digite o primeiro número: '))
b = int(input('Agora digite o segundo número: '))
opcao = 0   # Iniciar a opção como 0 para o usuário

def soma():
    resultado = a + b
    return f'Seu resultado é {resultado}' # Usando o return para armazenar os valores 


def subtracao():
    resultado = a - b
    return f'Seu resultado é {resultado}' # Usando o return para armazenar os valores 


def divisao():
    resultado = a / b
    return f'Seu resultado é {resultado} ' # Usando o return para armazenar os valores 


def multiplicacao():
    resultado = a * b
    return f'Seu resultado é {resultado}' # Usando o return para armazenar os valores 


def fatorial():
    resultado1 = math.factorial(a)
    resultado2 = math.factorial(b)
    return f'Seu resultado é {resultado1} e {resultado2}' # Usando o return para armazenar os valores 


x = soma()              # Colocando as funções em variaveis para depois printar nos if e elif
y = subtracao()         # Colocando as funções em variaveis para depois printar nos if e elif
z = divisao()           # Colocando as funções em variaveis para depois printar nos if e elif
w = multiplicacao()     # Colocando as funções em variaveis para depois printar nos if e elif
m = fatorial()          # Colocando as funções em variaveis para depois printar nos if e elif

while opcao != 6:       # Enquanto opção for diferente ou igual a 6, com isso mesmo se o usuário digitar 7, ira ter o looping
    print('''    [1] Somar  
    [2] Subtração
    [3] Divisão
    [4] Multiplicação
    [5] Fatorial
    [6] Sair''')        # ''' Usado no print para quebrar linhas
    opcao = int(input('Escolha sua opção: '))
    if opcao == 1:
        print(x)
    elif opcao == 2:
        print(y)
    elif opcao == 3:
        print(z)
    elif opcao == 4:
        print(w)
    elif opcao == 5:
        print(m)
    elif opcao == 6:
        print('Fim!')
    else:
        print('Opção inválida, por favor digite entre os números 1 a 6')



    
