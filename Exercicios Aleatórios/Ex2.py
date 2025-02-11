#Par ou Impar
n = float(input('Digite um numero para saber se é par ou impar: '))

resto = n % 2

if  resto == 0:
    print('Numero é par')
else:
    print('Numero é impar')    