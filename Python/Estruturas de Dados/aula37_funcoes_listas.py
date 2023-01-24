pc1 = 'HD Externo'
pc2 = 'SSD 480GB'
pc3 = 'GTX 1650'
pc4 = 'Intel i3 10th'
pc5 = '16 GB de RAM'
      # Eles são classificados por index, se for de trás para frente será números negativos

pcgamer = ['HD Externo', 'SSD 480GB', 'GTX 1650', 'Intel i3 10th', '16 GB de RAM']
    #           0               1           2               3               4  

#pcgamer.append('Placa mãe ASRock') Adiciona um item novo ao final da lista
#pcgamer.remove('HD Externo') Remove qualquer item da lista
#pcgamer.insert(0, 'HD 1TB') Adiciona qualquer item na posição desejada, neste caso foi no index 0
#pcgamer.pop(3) Remove qualquer index da lista
pcgamer.sort() # Coloca a lsita em ordem alfabética
print(pcgamer)        