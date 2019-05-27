#имя проекта: numpy-example
#номер версии: 1.0
#имя файла: example_5.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 27.04.2019
# дата последней модификации: 27.04.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Определить средние значения по всем строкам и
# столбцам матрицы. Результат оформить в виде матрицы из N + 1 строк и M
# + 1 столбцов.
#версия Python: 3.6

import numpy as np
import random

N = np.random.randint(2,10)
M = np.random.randint(2,10)

print(N,M)
A=np.random.randint(0,10, (N,M))

print(A)

M_mean = A.mean(axis=0)
N_mean = A.mean(axis=1)

print("Матрица со средними значениями-",A)


N_mean = np.append(N_mean, None)

A = np.vstack((A, M_mean))
A = np.hstack((A, N_mean.reshape(-1,1)))

print("Матрица с N и M +1-",A)
