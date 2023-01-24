compra_confirmada = True
dados = 'Compra no valor de 467.00 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados)
        print('Detalhes enviado para o seu email')
        break
else:
    print('Falha na compra')