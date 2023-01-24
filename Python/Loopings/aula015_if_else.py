velocidade = int(input('Digite a sua velocidade percorrida: '))

if velocidade > 110:
    print('Velocidade acima da média, favor diminuir!')
elif velocidade < 60:
    print('Velocidade muito abaixo da média, favor acelere!')
else:
    print('Velocidade OK!')
    