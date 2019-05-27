#имя проекта: numpy-example
#номер версии: 1.0
#имя файла: example_17.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 11.05.2019
# дата последней модификации: 11.05.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Добавить к матрице строку и вставить ее под
# номером L.
#версия Python: 3.6

import numpy as np
import random

N = np.random.randint(2,10)
M = np.random.randint(2,10)
L = 1
print(N,M)

matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

row = np.random.randint(low=-9, high=10, size=M)
print("Строка для вставки: {}".format(row))

matrix = np.insert(matrix, L, row, axis=0)
print("Полученная матрица:\r\n {}".format(matrix))