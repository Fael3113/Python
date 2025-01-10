#Verificação de numero par e multiplo de 3
n = float(input('Digite um numero: '))
resto = n % 2
restou = n % 3

if resto == 0 and restou ==0:
    print('O numero é par e multiplo de 3')
elif resto == 0:
    print('O numero é par')
elif restou == 0:
    print('O numero é multiplo de 3')
else:
    print('O numero não é multiplo de 3 e nem par')            