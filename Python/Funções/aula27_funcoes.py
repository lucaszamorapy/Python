a = int(input('Digite o primeiro número para o cálculo: '))
b = int(input('Digite o segundo número para o cálculo: '))
cal = int(input('Soma(1) ou Subtração(2): '))


def soma():
    resultado = a + b 
    print('Seu resultado é: {}'.format(resultado))


def subtracao():
    resultado = a - b
    print('Seu resultado é: {}'.format(resultado))


if cal == 1: # Se o usuário digitar 1 vai ser igual a função soma
    soma()

elif cal == 2:
    subtracao()

else:
    print('Digite 1 para soma e 2 para subtração') # Se o usuário digitar 2 vai ser igual a função subtração


