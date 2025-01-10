distancia = float(input('Digite a distancia percorrida em km:'))
gasolina = float(input('Digite o valor da gasolina: '))
consumo = float(input('Digite o consumo do carro em km/litro: '))
print('Distancia percorrida foi:', distancia)
print('Valor da gasolina foi: ', gasolina)
print('O consumo do carro foi: ', consumo)
gasto = (distancia*gasolina)/consumo
print('O carro gastou em media: ', gasto, ' reais')
