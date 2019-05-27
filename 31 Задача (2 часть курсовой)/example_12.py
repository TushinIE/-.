#имя проекта: numpy-example
#номер версии: 1.0
#имя файла: example_12.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 7.05.2019
# дата последней модификации: 7.05.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Разделить элементы каждой строки на элемент
# этой строки с наибольшим значением.
#версия Python: 3.6


import numpy as np
import random
N = random.randint(2, 5)
M = random.randint(2, 5)
print(N, M)
A = np.random.randint(-50, 50, (N,M))
A = np.array(A, float)

print(str(A) + "\n")

for i in range(N):
    mx = np.max(A[i, :])
    for k in range(M):
        if A[i, k] != mx:
            print(A[i, k] / mx)
            A[i, k] = round(A[i, k] / mx, 2)
print(A)
