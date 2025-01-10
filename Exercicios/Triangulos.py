print('Descobrindo que tipo de triangulo é')
num1 = float(input('Digite o valor da primeira aresta:'))
num2 = float(input('Digite o valor da segunda aresta:'))
num3 = float(input('Digite o valor da terceira aresta:'))
if (num1 == num2) and (num1 == num3) :
    print('Seu triangulo é Equilatero')
elif (num1==num2) or (num1==num2) or (num1==num2):
    print('Seu triangulo é Isósceles')
else:
    print('Seu triangulo é Escaleno')