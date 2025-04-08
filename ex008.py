n1 = float(input('Digite a primeira nota: '))
print('Primeira nota: ',n1)
n2 = float(input('Digite a segunda nota: '))
print('Segunda nota: ',n2)
media = (n1+n2)/2
print("Media: ", media)

if (media >= 7):
    print("Aprovado")
else:
    print(" Reprovado")