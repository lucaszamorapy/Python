#MENOR QUE 18,5 MAGREZA
#ENTRE 18,5 E 24,9 NORMAL
#ENTRE 25,0 E 29,9 SOBREPESO
#ENTRE 30,0 E 39,9 OBESIDADE
#MAIOR QUE 40,0 OBESIDADE GRAVE

alt = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é seu peso em kg: '))

imc =  peso / (alt/100)**2

if imc < 18.5:
    print(imc)
    print('Magreza, bora comer!!')
elif imc >= 18.5 and imc <= 24.5:
    print(imc)
    print('Ta normal paizão')
elif imc >= 25.0 and imc <= 29.9:
    print(imc)
    print('Mermão vai com calma, voce ta no sobrepeso')
elif imc >= 30.0 and imc <= 39.9:
    print(imc)
    print('Obesidade, bora pra academia!!')
else:
    imc > 40.0
    print(imc)
    print('Obesidade grave, vai de comes e bebes')
