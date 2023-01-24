# Criar classe
class Funcionarios:
    def __init__(self, nome, sobrenome, data_nasc):     # __init__ inicialização do contrutor
        self.nome = nome        # Self pega o valor do objeto, assim nao tendo que criar varios
        self.sobrenome = sobrenome
        self.data_nasc = data_nasc
        

# Criar objeto
funcionario1 = Funcionarios('Lucas', 'Zamora', '26/06/2003')                # Preenche os parametros com nome, sobrenome e data de nascimento
funcionario2 = Funcionarios('Matheus', 'Brasileiro Aguiar', '11/10/1993')

# Imprimir
print(funcionario1.nome)
print(funcionario1.sobrenome)
print(funcionario1.data_nasc)
print(funcionario2.nome)
print(funcionario2.sobrenome)
print(funcionario2.data_nasc)