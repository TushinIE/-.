def bubble(arr, dim):
    alg_count = [0, 0]
    for i in range(dim - 1):
        for j in range(dim - i - 1):
            alg_count[0] += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                alg_count[1] += 1
    return alg_count
