print("Verificando se o número é maior, menor ou igual")
a = float(input("Digite o número A "))
b = float(input("Digite o número B "))
    
if (a>b):
    print("O número A {} é maior que o número B {}".format (a, b))
elif (a<b):
    print("O número A {} é menor que o número B {}".format (a, b))
else:
    print("Ambos A e B são iguais")