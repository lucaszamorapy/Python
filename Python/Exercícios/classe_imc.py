from datetime import datetime

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nasc, altura, peso, imc=0):     # __init__ inicialização do contrutor
        self.nome = nome        # Self pega o valor do objeto, assim nao tendo que criar varios
        self.sobrenome = sobrenome
        self.ano_nasc = ano_nasc
        self.altura = altura
        self.peso = peso
        self.imc = imc
    
    def nome_compelto(self):                        # Usa-se o self dentro da função pelo fato dele agregar o objeto "funcionario(x)"
        return self.nome + ' ' + self.sobrenome    # retornar nome mais o sobrenome do funcionario


    def idade_funcionario(self):
        ano_atual = datetime.now().year                 # Declarando a variavel ano_atual com datetime
        self.ano_nasc = int(ano_atual - self.ano_nasc)  # atribuindo no self.ano_nasc o cálculo 
        return self.ano_nasc                            # armazenando o valor do cálculo


    def imc_funcionario(self):
        self.imc = self.peso / (self.altura/100)**2
        if self.imc < 18.5:
            return f'Magreza'

        elif self.imc >= 18.5 and self.imc <= 24.5:
            return f'Normal'

        elif self.imc >= 25.0 and self.imc <= 29.9:
            return f'Sobrepeso'

        elif self.imc >= 30.0 and self.imc <= 39.9:
            return f'Obesidade'

        else:
            self.imc > 40.0
            return f'Obesidade grave'
            
# Criar objeto
funcionario1 = Funcionarios('Lucas', 'Zamora', 2003, 180, 90)                # Preenche os parametros com nome, sobrenome e data de nascimento
funcionario2 = Funcionarios('Matheus', 'Brasileiro Aguiar', 1993, 176, 70)

# Imprimir
print(f'O IMC do funcionário é {Funcionarios.imc_funcionario(funcionario1)}')
print(f'O IMC do funcionário é {Funcionarios.imc_funcionario(funcionario2)}')
# Entre na classe funcionarios, na função imc_funcionario do objeto funcionario1 e funcionario2