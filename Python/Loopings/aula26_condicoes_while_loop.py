# Publicar um produto com comissão de 10% se for acima de R$20

valor = int(input('Digite o valor do seu produto em R$: '))
while valor > 20:
    valor = (valor * 0.10) + valor
    print('O valor da comissão de 10% é R$ {} reais'.format(valor))
    break