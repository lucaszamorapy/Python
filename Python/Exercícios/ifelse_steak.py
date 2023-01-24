temp = int(input('Qual seria a temperatura da sua carne? '))

if temp <= 47:
    print('Cozinhe mais a carne')
elif temp <= 53:
    print('Carne esta selada')
elif temp <= 59:
    print('Carne ao ponto para o mal')
elif temp <= 64:
    print('Ao ponto')
elif temp <= 70:
    print('Ao ponto para o bem')
elif temp <= 79:
    print('Bem passada')
else:
    print('Carne está queimada')