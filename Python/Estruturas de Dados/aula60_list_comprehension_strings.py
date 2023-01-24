# Mais simples de se escrever
# Utilizado quando voce precisa criar uma nova lista a partir de uma existente
# [expressao for iten in itens]

nomes1 = ['Lucas', 'Leticia', 'Bruno', 'Matheus', 'Marcos']
nomes2 = []

#For loop
for iten in nomes1 :
    if 'L' in iten: 
        nomes2.append(iten)
print(nomes2)

#List Comprehsion
nomes2 = [iten for iten in nomes1 if 'M' in iten]
print(nomes2)  #Só colocar uma expressão e depois todo o looping com o if dentro da lista
