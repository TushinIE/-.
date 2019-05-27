#имя проекта: numpy-example
#номер версии: 1.0
#имя файла: example_3.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 27.04.2019
# дата последней модификации: 27.04.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Найти наименьший элемент столбца матрицы A,
# для которого сумма абсолютных значений элементов максимальна.
#версия Python: 3.6

import numpy as np
import random

N= random.randint (1,10)
M= random.randint (1,10)

print(N,M)
A=np.random.randint(0,10, (N,M))

print(A)

mx=0
indmx=0
for i in range (M):
    if np.sum(A[:, i])>mx:
        mx = np.sum(A[:, i])
        indmx=i
print("Столбец с максимальной суммой элементов-"+ str(A[: , indmx]))
print("Сумма этого столбца-"+str(mx)+ ","+ "номер этого столбца-"+ str(indmx+1))
stmin=10
for b in A [: , indmx]:
    if b< stmin:
        stmin=b
print("Минимальный элемент этого столбца-"+str(stmin))