#имя проекта: numpy-example
#номер версии: 1.0
#имя файла: example_29.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 20.05.2019
# дата последней модификации: 20.05.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Добавить к матрице столбец чисел и вставить его
# под номером K.
#версия Python: 3.6

import numpy as np
import random

N= random.randint (1,10)
M= random.randint (1,10)
K=1
print(N,M)

matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

col = np.random.randint(low=-9, high=10, size=N)
print("Столбец для вставки: {}".format(col))

matrix = np.insert(matrix, K, col, axis=1)
print("Полученная матрица:\r\n {}".format(matrix))