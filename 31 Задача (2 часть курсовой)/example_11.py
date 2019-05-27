#имя проекта: numpy-example
#номер версии: 1.0
#имя файла: example_11.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 7.05.2019
# дата последней модификации: 7.05.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Просуммировать элементы каждой строки
# матрицы с соответствующими элементами L-й строки.
#версия Python: 3.6

import numpy as np
import random
N = random.randint(2, 5)
M = random.randint(2, 5)
print(N, M)
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

L = random.randint(0, N)
print("L = " + str(L + 1))
L_m = A[L, :].flat

for i in range(N):
    if i != L:
        for k in range(M):
            A[i, k] = A[i, k] + L_m[k]
print(A)
