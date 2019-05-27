#имя проекта: numpy-example
#номер версии: 1.0
#имя файла: example_15.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 10.05.2019
# дата последней модификации: 10.05.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Все элементы имеют целый тип. Дано целое число
# H. Определить, какие столбцы имеют хотя бы одно такое число, а какие не
# имеют.
#версия Python: 3.6

import numpy as np
import random

N = np.random.randint(2,10)
M = np.random.randint(2,10)
H = 2
print(N,M)

matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

matrix_bool = matrix == H
row_sum = np.sum(matrix_bool, axis=0)

print("Столбцы в которых встречается значение {}:".format(H))
print(np.argwhere(row_sum).flatten())

print("Столбцы в которых нет значения {}:".format(H))
print(np.argwhere(row_sum == 0).flatten())
