# Filter faz a mesma coisa que o map porém ele retira o resultado da função
# Remover valores acima de 50


valores = [10, 20, 50, 70, 170]

def remover50 (x):
        return x <= 50

print(list(filter(remover50, valores)))
print(list(filter(lambda x: x <= 50, valores))) # Lembre-se com o lambda sempre tem que ter o argumento e a "função"

