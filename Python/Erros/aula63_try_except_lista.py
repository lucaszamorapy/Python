# Erros
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

try: 
    letras = ['a','b','c']
#Index         0   1   2
    print(letras[3])         # O index 3 não existe
except IndexError:
    print('Index não existe')