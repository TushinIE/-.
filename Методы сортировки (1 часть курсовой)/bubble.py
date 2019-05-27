def bubble(arr, dim):
    alg_count = [0, 0]
    for i in range(dim - 1):
        alg_count[0] += 1
        for j in range(dim - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                alg_count[1] += 1
    print(alg_count)
import random
arry = [random.randint(0, 20) for i in range(20)]
print(arry)
bubble(arry, len(arry))
print(arry)