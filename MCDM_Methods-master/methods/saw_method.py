


def __count__(row, weights):
    '''
    Метод подсчета суммы произведений матрицы на веса
    :param row: строка матрицы данных
    :param weights: список весов
    :return: сумма произведений матрицы на веса
    '''
    return sum([row[i] * weights[i] for i in range(len(row))])


def saw_method(dataset: list[list], weights: list):
    '''
    SAW метод для сравнения альтернатив по весам
    :param dataset: исходные данные
    :param weights: список весов
    :return: список ценности альтернатив
    '''
    browsers = ['Google Chrome', 'Safari', 'Амиго', 'Tor browser', 'Microsoft Edge', 'Enternet Explorer']
    max_score = 0
    max_score_ind = 0
    res = []
    print('\n---------SAW METHOD---------\n')
    for ind, elem in enumerate(dataset):
        c = round(__count__(elem, weights), 3)
        if c > max_score:
            max_score = c
            max_score_ind = ind
        res.append(c)
        print(f'<{browsers[ind]}> has score: {c}')
    print(f'\n<{browsers[max_score_ind]}> is better than others. It has score: {max_score}')
    return res
