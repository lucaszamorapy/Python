# import funcoes
from funcoes import soma, multi
from items.cadastro import cliente
# Do pacote items cadastro importa cliente

# funcoes.soma()
# funcoes.multi()
soma()
multi()
cliente()


# Temos duas formas para importar as funções
# Import = ele importa TODAS as funções
# From Import = importa a função específica, from (nome do módulo) import (nome da função)
# Com pacotes = cria uma pasta chamada items, dentro dela coloca suas funçoes e cria um arquivo '__init__.py'
# Assim o Python reconhece que aquela pasta items é um pacote