a = int(input('Digite o primeiro número para o cálculo: '))
b = int(input('Digite o segundo número para o cálculo: '))
cal = int(input('Soma(1) ou Subtração(2): '))


def soma():
    resultado = a + b 
    return 'Seu resultado é: {}'.format(resultado) # O return armazena o valor da variavel resultado, porem nao imprime


def subtracao():
    resultado = a - b
    return 'Seu resultado é: {}'.format(resultado) # O return armazena o valor da variavel resultado, porem nao imprime


x = soma() # Criei variavel x para poder imprimir o resultado da função soma() no if
y = subtracao() # Criei variavel y para poder imprimir o resultado da função subtração() no elif

if cal == 1: 
   
    print(x) # Aqui esta dizendo "se cal for igual a 1, retornar a funcao soma e seu resultado"

elif cal == 2:
    
    print(y) # Aqui esta dizendo "se cal for igual a 2, retornar a funcao subtracao e seu resultado"

else:
    print('Digite 1 para soma e 2 para subtração') 


''' Obs: no outro código de função chamamos as funcoes soma() e subtraçao() no if e no elif, neste agora apenas
declaramos as funcoes como x e y e pedimos para imprimir no if elif. 
'''