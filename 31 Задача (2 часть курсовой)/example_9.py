#имя проекта: numpy-example
#номер версии: 1.0
#имя файла: example_9.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 5.05.2019
# дата последней модификации: 5.05.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Определить, сколько нулевых элементов
# содержится в верхних L строках матрицы и в левых К столбцах матрицы.
#версия Python: 3.6


import numpy as np

N = np.random.randint(2,10)
M = np.random.randint(2,10)
L = np.random.randint(1,N)
K = np.random.randint(1,M)

print(N,M,L,K)
A=np.random.randint(-10,10, (N,M))

New_A = A[:L, :K]

print(A)

print(np.sum(New_A == 0))