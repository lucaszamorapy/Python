# Da para entender melhor se levarmos como um if else de erros

valor = 0
while valor == 0:                                  # Enquanto o valor for inteiro
    try:
        valor = int(input('Digite o valor a ser descontado em 5%: '))      # Tente
        resultado = lambda valor:  valor - (valor * 0.05) 
        print('O valor com 5% é: {}'.format(resultado(valor)))
        break
    except ValueError:                                              # Senão
        print('Tem que ser em número porra!!')




        