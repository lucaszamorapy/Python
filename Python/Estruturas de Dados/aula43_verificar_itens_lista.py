print('====== ELETRONICOS E CIA ======')

print('         BEM-VINDO      ')
pedido = input('Qual item voce deseja? ')
item = ['HD EXTERNO 1TB', 'RTX 4090', 'INTEL I7', 'GTX 1050 TI','SSD KINGSTON 280GB','T-FORCE 8GB RAM']

if pedido.upper() in item:              # Usei o upper para quando o usuário digitar ir sempre em maiusculo, para validar no python
    print(f'Temos em o estoque')
else:
    print('Infelizmente não temos em estoque')
