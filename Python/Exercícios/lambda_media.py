n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a tericera nota: '))
n4 = int(input('Digite a quarta nota: '))

resultado = lambda n1,n2,n3,n4: (n1 + n2 + n3 + n4) / 4

print(resultado(n1,n2,n3,n4))