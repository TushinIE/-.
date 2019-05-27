#имя проекта: numpy-example
#номер версии: 1.0
#имя файла: example_18.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 12.05.2019
# дата последней модификации: 12.05.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Найти сумму элементов, стоящих на главной
# диагонали, и сумму элементов, стоящих на побочной диагонали (элементы
# главной диагонали имеют индексы от [0,0] до [N,N], а элементы побочной
# диагонали — от [N,0] до [0,N]).
#версия Python: 3.6

import numpy as np
import random

N = np.random.randint(2,10)
M = np.random.randint(2,10)

print(N,M)

matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

diagonal_main = np.diagonal(matrix)
print("Элементы главной диагонали:\r\n{}".format(diagonal_main))

sum_diagonal_main = np.sum(diagonal_main)
print("Cумма элементов главной диагонали:\r\n{}".format(sum_diagonal_main))

diagonal_side = np.diagonal(matrix[::-1])
print("Элементы побочной диагонали:\r\n{}".format(diagonal_side))

sum_diagonal_side = np.sum(diagonal_side)
print("сумму элементов побочной диагонали:\r\n{}".format(sum_diagonal_side))
