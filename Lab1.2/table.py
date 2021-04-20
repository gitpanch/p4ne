from matplotlib import pyplot
from openpyxl import load_workbook
def getvalue(x):
    return x.value

wb = load_workbook('data_analysis_lab.xlsx')

cell = wb['Data']
y = list(map(getvalue, cell['A'][1:]))
t = list(map(getvalue, cell['C'][1:]))
a = list(map(getvalue, cell['D'][1:]))
pyplot.plot(y, t, label="Температура")
pyplot.plot(y, a, label="Активность")
pyplot.show()
