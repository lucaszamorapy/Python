# Else voce so usa quando quer que o resultado do try de positivo
# Finally voce usa quando quer que mostre tanto no resultado positivo ou negativo 


valor = 0
while valor == 0:                                 
    try:
        valor = int(input('Digite o valor a ser descontado em 5%: '))  # Tente ler se o input é igual a int
    except ValueError:                                              
        print('Tem que ser em número porra!!')          # Se der o erro de value, imprima isso na tela
    else:
        resultado = lambda valor:  valor - (valor * 0.05)   # Senão der erro, faça o desconto do valor
        print('O valor com 5% é: {}'.format(resultado(valor)))
        break
    '''finally:                             
        print('Parabéns mascuaico!!')'''
