# Criar classe
class Funcionarios:
    def __init__(self, nome, sobrenome, data_nasc):     # __init__ inicialização do contrutor
        self.nome = nome        # Self pega o valor do objeto, assim nao tendo que criar varios
        self.sobrenome = sobrenome
        self.data_nasc = data_nasc
    
    def nome_completo(self):                        # Usa-se o self dentro da função pelo fato dele agregar o objeto "funcionario(x)"
        return self.nome + ' ' + self.sobrenome     # retornar nome mais o sobrenome do funcionario

        

# Criar objeto
funcionario1 = Funcionarios('Lucas', 'Zamora', '26/06/2003')                # Preenche os parametros com nome, sobrenome e data de nascimento
funcionario2 = Funcionarios('Matheus', 'Brasileiro Aguiar', '11/10/1993')

# Imprimir
print(Funcionarios.nome_completo(funcionario1))
# Entre na classe funcionarios, na função nome_completo do objeto funcionario1