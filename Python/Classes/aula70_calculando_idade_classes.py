from datetime import datetime

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nasc):     # __init__ inicialização do contrutor
        self.nome = nome        # Self pega o valor do objeto, assim nao tendo que criar varios
        self.sobrenome = sobrenome
        self.ano_nasc = ano_nasc
    
    def nome_compelto(self):                        # Usa-se o self dentro da função pelo fato dele agregar o objeto "funcionario(x)"
        return self.nome + ' ' + self.sobrenome    # retornar nome mais o sobrenome do funcionario

    def idade_funcionario(self):
        ano_atual = datetime.now().year                 # Declarando a variavel ano_atual com datetime
        self.ano_nasc = int(ano_atual - self.ano_nasc)  # atribuindo no self.ano_nasc o cálculo 
        return self.ano_nasc                            # armazenando o valor do cálculo

# Criar objeto
funcionario1 = Funcionarios('Lucas', 'Zamora', 2003)                # Preenche os parametros com nome, sobrenome e data de nascimento
funcionario2 = Funcionarios('Matheus', 'Brasileiro Aguiar', 1993)

# Imprimir
print(f'Tem {Funcionarios.idade_funcionario(funcionario1)} anos')
print(f'Tem {Funcionarios.idade_funcionario(funcionario2)} anos')
# Entre na classe funcionarios, na função idade_funcionario do objeto funcionario1 e funcionario2