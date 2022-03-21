import numpy as np
from DecisionHelper import DecisionHelper
from prettytable import PrettyTable


def print_table():
    characters = ['', 'Стоимость ' + str(wei[0]), 'Использование ресурсов ' + str(wei[1]),
                  'Удовлетворенность ' + str(wei[2]),
                  'Защищенность ' + str(wei[3]), 'Полнота контекста ' + str(wei[4]), 'Модифицируемость ' + str(wei[5]),
                  'Переносимость ' + str(wei[6])]
    browsers = ['Google Chrome', 'Safari', 'Амиго', 'Tor browser', 'Microsoft Edge', 'Enternet Explorer']
    table = PrettyTable()
    table.field_names = characters
    for i in range(5):
        table.add_row([browsers[i], m[i][0], m[i][1], m[i][2], m[i][3], m[i][4], m[i][5], m[i][6]])
    print(table)


if __name__ == '__main__':
    m = np.array([[1, 0.65, 0.91, 0.91, 0.93, 0.92, 0.93],
                  [1, 0.88, 0.91, 0.95, 0.85, 0.75, 0.76],
                  [1, 0.67, 0.62, 0.65, 0.63, 0.68, 0.67],
                  [1, 0.72, 0.92, 0.98, 0.74, 0.73, 0.67],
                  [1, 0.85, 0.87, 0.91, 0.89, 0.86, 0.83],
                  [1, 0.71, 0.83, 0.81, 0.69, 0.71, 0.78]])
    wei = [0.14, 0.16, 0.19, 0.17, 0.12, 0.12, 0.1]

    print_table()
    dh = DecisionHelper(m, wei)
    print(dh.saw())
    print(dh.topsis())
    print(dh.electre())
