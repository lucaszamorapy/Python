pc1 = 'HD Externo'
pc2 = 'SSD 480GB'
pc3 = 'GTX 1650'
pc4 = 'Intel i3 10th'
pc5 = '16 GB de RAM'
pc6 = 'Fonte 550W'
pc7 = 'Placa mãe ASRock'                
pc8 = 'Gabinete Preto'       # Eles são classificados por index, se for de trás para frente será números negativos

pcgamer = ['HD Externo', 'SSD 480GB', 'GTX 1650', 'Intel i3 10th', '16 GB de RAM', 'Fonte 550W', 'Placa mãe ASRock', 'Gabinete Preto']
    #           0               1           2               3               4           5                   6               7


'''print(pcgamer[2]) # Estou puxando apenas o item de index 2 para imprimir'''
pcgamer[3] = 'Intel i9'  # Mudei a lista, trocando o nome do index 3
print(pcgamer)
