funcionarios = {'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'}
turno_dia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
turno_noite = {'Pedro', 'Sophia', 'Bruno'}
tem_carro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

set1 = turno_noite.intersection(tem_carro)
print(set1)

set2 = turno_dia.intersection(tem_carro)
print(set2)

set3 = funcionarios.difference(tem_carro)
print(set3)

