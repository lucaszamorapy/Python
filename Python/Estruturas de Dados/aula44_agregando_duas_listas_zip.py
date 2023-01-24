nome1 = input('Digite o nome da primeira pessoa: ')
idade1 = input('Digite a idade da primeira pessoa: ')
sexo1 = input('Digite o sexo da primeira pessoa: ')
nome2 = input('Digite o nome da segunda pessoa: ')
idade2 = input('Digite a idade da segunda pessoa: ')
sexo2 = input('Digite o sexo da segunda pessoa: ')
nome3 = input('Digite o nome da terceira pessoa: ')
idade3 = input('Digite a idade da terceira pessoa: ')
sexo3 = input('Digite o sexo da terceira pessoa: ')

nomes = [nome1, nome2, nome3]
idades = [idade1, idade2, idade3]
sexos = [sexo1, sexo2, sexo3]

tres_listas = zip(nomes, idades, sexos)         # Zip serve para juntar uma lista na outra, junto com o list

print(list(tres_listas))
