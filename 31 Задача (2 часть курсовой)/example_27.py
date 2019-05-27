#номер версии: 1.0
#имя файла: example_27.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 19.05.2019
# дата последней модификации:19.05.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Все элементы имеют целый тип. Дано целое число
# H. Определить, какие строки имеют хотя бы одно такое число, а какие не
# имеют.
#версия Python: 3.6

import numpy as np

N = 6
M = 7

H = 2


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

matrix_bool = matrix == H
col_sum = np.sum(matrix_bool, axis=1)

print("Строки в которых встречается значение {}:".format(H))
print(np.argwhere(col_sum).flatten())

print("Строки в которых нет значения {}:".format(H))
print(np.argwhere(col_sum == 0).flatten())
