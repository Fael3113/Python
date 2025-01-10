#Fatorial
n = float(input('Digite um numero: '))
r = 1
c = 1

while c <= n:
    r *= c
    c += 1

print (r)