rend = int(input('Digite o rendimento da tinta: '))
alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))

def cal():
    area = alt * larg
    tinta = lambda area, rend : area / rend
    return f'Voce precisa de {tinta(area, rend)} latas de tinta'

x = cal()

print(x)