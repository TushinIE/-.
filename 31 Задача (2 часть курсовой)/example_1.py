#имя проекта: numpy-example
#номер версии: 1.0
#имя файла: example_1.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 27.04.2019
# дата последней модификации: 27.04.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Найти наибольший элемент столбца матрицы A,
# для которого сумма абсолютных значений элементов максимальна.
#версия Python: 3.6

import numpy as np
import random

N= random.randint (1,10)
M= random.randint (1,10)

print(N,M)

A=np.random.randint(0,100, (N,M))

print(A)

mx=0
indmx=0
for i in range (M):
    if np.sum(A[:, i])>mx:
        mx = np.sum(A[:, i])
        indmx=i
print("Столбец с максимальной суммой элементов-"+ str(A[: , indmx]))
print("Сумма этого столбца-"+str(mx)+ ","+ "номер этого столбца-"+ str(indmx+1))
stmax=0
for b in A [: , indmx]:
    if b> stmax:
        stmax=b
print("Максимальный элемент этого столбца-"+str(stmax))