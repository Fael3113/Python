#Calculadora de IMC
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso/(altura*altura)

if imc < 18.49:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc <= 24.99: 
    print('Você está com o peso ideal')
elif imc >= 25 and imc <= 29.99:
    print('Você está com sobrepeso')
else:
    print('Você está em estado de obesidade')       