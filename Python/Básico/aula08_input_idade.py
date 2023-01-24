'''Na variável idade tinha dado um erro pois o Python não consegue calcular um int com uma str, por isso temos que
converter a variável ano_Nasc em int '''

ano_Nasc = input('Digite o ano que voce nasceu: ')
idade = 2023 - int(ano_Nasc)

print('Voce tem {} anos de idade'.format(idade))

