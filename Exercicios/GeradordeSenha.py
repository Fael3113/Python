import random

print("Gerador de senha com Python")

letra = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q' ,'R', 'S', 'T', 'U', 'V', 'W', 'X' ,'Y', 'Z']

simbolo = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numero = ['0','1','2','3','4','5','6','7','8','9']

num_let = int(input("Quantas letras gostaria em sua senha?\n "))
num_num = int(input("Quantos números gostaria em sua senha?\n "))
num_simb = int(input("Quantos símbolos gostaria em sua senha?\n "))
escolha = int(input('''Que tipo de senha gostaria de criar?
\n1 Para ordem "Letra + Numero + Simbolo" da senha
\n2 Para senha randomica
\nSelecione: '''))

lista = ""
for n in range(1, num_let+1):
  lista = lista + letra[random.randint(0, len(letra)-1)] 
for n in range(1, num_num+1):
  lista = lista + numero[random.randint(0, len(numero)-1)]
for n in range(1, num_simb+1):
  lista += simbolo[random.randint(0, len(simbolo)-1)]

if (escolha == 1):
  print(f'A senha é: {lista}')

elif (escolha == 2):
  pass_ran =""
  segredo =[]

  for n in range(0, len(list)):
    segredo.extend(lista[n])

  counter = 0
  for n in range(0, len(segredo)):
    counter = random.randint(0, len(segredo)-1)
    pass_ran = pass_ran + segredo[counter]
    segredo.remove(segredo[counter])
  print(f'A senha é: {pass_ran}')
  
else:
  print("Opção invalida. Por favor, tente novamente!")

