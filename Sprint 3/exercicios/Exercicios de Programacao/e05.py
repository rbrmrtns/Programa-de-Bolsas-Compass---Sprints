from datetime import date

dia = 22
mes = 10
ano = 2022

data = date(ano, mes, dia)

print(str(data.day) + '/' + str(data.month) + '/' + str(data.year))
