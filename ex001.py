import datetime as date

data_atual = date.datetime.now()

dia_da_semana = data_atual.strftime('%A')

print(dia_da_semana)

if dia_da_semana == 'Tuesday':
    print("Vai chover")
else:
    print("Vai fazer sol") 