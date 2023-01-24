'''valores = []

for x in range(1, 7):       For loop
    valores.append(x * 10)  Expressão
print(valores)'''


valores = [x * 10 for x in range(1, 7)]     # Imagine que o list comprehsion faz toda sua expressao dentro da lista direto
print(valores)                              # Todo o for loop esta dentro dele

imp_par = [x % 2 for x in range(1, 7)]
print(imp_par)

