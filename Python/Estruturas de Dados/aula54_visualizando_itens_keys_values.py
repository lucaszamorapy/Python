aluno = {'nome': 'Paula', 
        'idade': '22 anos', 
        'nota_final': 9, 
        'aprovação': True, 
        'Matérias': ['História', 'Geografia', 'Portugues']}

print(aluno)

print(aluno.get('Matérias')) # Imprime os values da key Máterias
print(len(aluno)) # Imprime quantas keys tem no dicionario
print(aluno.keys()) # Imprime somente as keys do dicionario
print(aluno.items()) # Imprime keys e values do dicionario
print(aluno.values()) # Imprime somente os valores das keys