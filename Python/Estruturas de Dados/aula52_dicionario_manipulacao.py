aluno = {'nome': 'Paula', 'idade': '22 anos', 'nota_final': 9, 'aprovação': True}

aluno ['nome'] = 'Jose' # Primeira forma de mudar o value da key
aluno.update({'nome': 'Ana', 'nota_final': 7}) # Nesta forma voce pode mudar quantas vezes voce quiser apenas em uma linha
aluno.update({'endereço': 'Rua Adolfo Cavalcanti'}) # Tambem pode adicionar novas keys com outros values
print(aluno.get('estado_civil','Não Existe')) # Get tambem serve para voce pegar algo do dicionario, ate mesmo coisas que nao existe
print(aluno.get('nome'))
del aluno['idade'] # Deleta uma key com seu value dentro do dicionario
print(aluno)