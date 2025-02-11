print("Calculadora com 2 números distintos")

def calculadora():

    operation = input('''Digite o modo de operação: 
*(multiplicação) 
/(divisão) 
+(adição) 
-(subtração)
**(elevado a)
''')

    n1 = float(input("Digite um número "))
    n2 = float(input("Digite um número "))

    if operation == '+':
        print("{} + {} = ".format (n1, n2))
        print(n1+n2)
    elif operation == '-':
        print('{} - {} = '.format (n1, n2))
        print(n1-n2)

    elif operation == '*':
        print('{} * {} = '.format (n1, n2))
        print(n1*n2)

    elif operation == '/':
        print('{} / {} = '.format (n1, n2))
        print(n1/n2)
    
    elif operation == '**':
        print('{} ** {} = '.format (n1, n2))
        print(n1**n2)

    else:
        print("Essa operação é inválida")
    again()
def again():
    calc_again = input("Deseja usar a calculadora novamente? Digite 1 para Sim e 2 para Não: ")

    if calc_again == '1':
        calculadora()
    elif calc_again == '2':
        print('Até mais')
    else:
        again()

calculadora()