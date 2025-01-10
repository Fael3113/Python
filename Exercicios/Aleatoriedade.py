from random import randint

x = []

for i in range(10):
    x.append(randint(0, 100))

print(x)
y = set(x)
print(y)

print("A lista tem {} números de 0 a 10000 aleatórios, e há {} números sem repetição". format(len(x), len(y)))
