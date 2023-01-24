aluno = {'nome': 'Paula', 'idade': '22 anos', 'nota_final': 9, 'aprovação': True}

'''for x in aluno:     Este looping só imprime as keys
    print(x)'''

'''for x in aluno.values():    Este looping só imprime os values
    print(x)'''

'''for x in aluno.keys():    Tambem imprime só as keys mas de um jeito organizado
    print(x)'''

'''for x in aluno.items():      Podemos ver que esse imprime todos porém em Tuples  
    print(x)'''

for keys, values in aluno.items():   # Ele esta tirando os itens de dentro da Tuple, atraves das variaveis keys e values
    print(keys, values)