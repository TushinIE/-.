#имя проекта: numpy-example
#номер версии: 1.0
#имя файла: example_10.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 5.05.2019
# дата последней модификации: 5.05.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Перемножить элементы каждого столбца матрицы
# с соответствующими элементами K-го столбца.
#версия Python: 3.6

import numpy as np
import random
N = random.randint(2, 5)
M = random.randint(2, 5)
print(N, M)
A = np.random.randint(-50, 50, (N, M))
print(str(A) + "\n")

K = random.randint(0, M)
print("K = " + str(K + 1))
K_m = A[:, K].flat

for i in range(M):
    if i != K:
        for k in range(N):
            A[k, i] = A[k, i] * K_m[k]
print(A)



