#Soma de numeros pares
n = int(input('Digite um numero par: '))
i = 0
soma = 0
while i < n:
    i = i + 2 
    print(i)
for i in range(2, n+1, 2):
    soma += i   

print('A soma dos números pares de 1 até', n, 'é:', soma)
    