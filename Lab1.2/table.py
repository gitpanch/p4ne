from matplotlib import pyplot
from openpyxl import load_workbook


def getvalue(x):
    return x.value


wb = load_workbook('data_analysis_lab.xlsx')

cell = wb['Data']

years = list(map(getvalue, cell['A'][1:]))
temp = list(map(getvalue, cell['C'][1:]))
activ = list(map(getvalue, cell['D'][1:]))

pyplot.plot(years, temp, label="Температура")
pyplot.plot(years, activ, label="Активность")

pyplot.xlabel('Годы')
pyplot.ylabel('Температура/Активность Солнца')
pyplot.legend(loc='upper left')

pyplot.show()
