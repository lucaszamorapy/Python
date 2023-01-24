alcance = 0
vertical = 6
simbolo = '*'

for v in range(vertical):
    alcance += 1
    for a in range(alcance):
        print(f'  {simbolo}', end='')
    print()