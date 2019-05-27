import numpy


def FancyPrint(A, B, selected):
    for row in range(len(B)):
        print("(", end='')
        for col in range(len(A[row])):
            print("\t{1:10.2f}{0}".format(" " if (selected is None or selected != (row, col)) else "*", A[row][col]), end='')
            print("\t) * (\tX{0}) = (\t{1:10.2f})".format(row + 1,
            B[row]))


data = numpy.genfromtxt('./numpy-gauss.csv', delimiter=';')

matrix_list = []
matrix = []
for row in data:
    first_col = row[0]
    if numpy.isnan(first_col):
        matrix_list.append(matrix)
        matrix = []
        continue

    mask = ~numpy.isnan(row)
    matrix.append(row[mask])
matrix_list.append(matrix)


f = open('numpy-gauss-slv.csv', 'wb+')
f.truncate()
for matrix in matrix_list:
    M = numpy.array(matrix)
    myA = numpy.delete(M, M.shape[1] - 1, axis=1)
    myB = M[:, [-1]].flatten()
    print("Исходная система:")
    FancyPrint(myA, myB, None)
    slv = numpy.linalg.solve(myA, myB)
    print("Решаем:")
    print(slv)
    numpy.savetxt(f, numpy.array([slv]), delimiter=',')
f.close()












































