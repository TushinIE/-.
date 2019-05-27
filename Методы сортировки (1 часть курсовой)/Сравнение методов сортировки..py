import random
import select_2
import bubble_2
import insert_2

DIM = 65
bubble_arr = []
insert_arr = []
select_arr = []
CTotal = [0, 0, 0]
MTotal = [0, 0, 0]

for i in range(1, DIM+1):
    bubble_arr.append(i)
    insert_arr.append(i)
    select_arr.append(i)

file = open("Result.txt", "w")
print("Упорядоченный массив: ")
print(bubble_arr)


count = select_2.select(select_arr, DIM)
print("Упорядоченный массив: результат")
print(select_arr)

CTotal[0] = count[0]
MTotal[0] = count[1]


count = insert_2.insert(insert_arr, DIM)
CTotal[1] = count[0]
MTotal[1] = count[1]


count = bubble_2.bubble(bubble_arr, DIM)
CTotal[2] = count[0]
MTotal[2] = count[1]
print("Размер массива:", DIM)
print("Сравнений:", CTotal[0], CTotal[1], CTotal[2])
print("Перестановок:", MTotal[0], MTotal[1], MTotal[2])

file.write("Упорядоченный массив:\n ")
file.write("Размер массива: " + str(DIM) + "\n")
file.write("Сравнений: " + str(CTotal[0]) + " " + str(CTotal[1]) + " " + str(CTotal[2]) + "\n")
file.write("Перестановок: " + str(MTotal[0]) + " " + str(MTotal[1]) + " " + str(MTotal[2]) + "\n")

select_arr.clear()
bubble_arr.clear()
insert_arr.clear()

for i in range(DIM, 0, -1):
    bubble_arr.append(i)
    insert_arr.append(i)
    select_arr.append(i)

print("Обратно упорядоченный массив: ")
print(bubble_arr)


count = select_2.select(select_arr, DIM)
print("Обратно упорядоченный массив: результат")
print(select_arr)

CTotal[0] = count[0]
MTotal[0] = count[1]


count = insert_2.insert(insert_arr, DIM)
CTotal[1] = count[0]
MTotal[1] = count[1]


count = bubble_2.bubble(bubble_arr, DIM)
CTotal[2] = count[0]
MTotal[2] = count[1]
print("Размер массива:", DIM)
print("Сравнений:", CTotal[0], CTotal[1], CTotal[2])
print("Перестановок:", MTotal[0], MTotal[1], MTotal[2])

file.write("Обратно упорядоченный массив:\n ")
file.write("Размер массива: " + str(DIM) + "\n")
file.write("Сравнений: " + str(CTotal[0]) + " " + str(CTotal[1]) + " " + str(CTotal[2]) + "\n")
file.write("Перестановок: " + str(MTotal[0]) + " " + str(MTotal[1]) + " " + str(MTotal[2]) + "\n")

KOL = 2000
CTotal = [0, 0, 0]
MTotal = [0, 0, 0]

for n in range(0, KOL):
    select_arr.clear()
    insert_arr.clear()
    bubble_arr.clear()

    select_arr = [random.randint(0, 100) for i in range(DIM)]
    for i in range(0, DIM):
        bubble_arr.append(select_arr[i])
        insert_arr.append(select_arr[i])


    count = select_2.select(select_arr, DIM)
    CTotal[0] += count[0]
    MTotal[0] += count[1]


    count = insert_2.insert(insert_arr, DIM)
    CTotal[1] += count[0]
    MTotal[1] += count[1]


    count = bubble_2.bubble(bubble_arr, DIM)
    CTotal[2] += count[0]
    MTotal[2] += count[1]

print("\nСлучайный массив:")
print("Проведено экспериментов:", KOL)
print("Размер массива:", DIM)
print("Сравнений:", CTotal[0]/KOL, CTotal[1]/KOL, CTotal[2]/KOL)
print("Перестановок:", MTotal[0]/KOL, MTotal[1]/KOL, MTotal[2]/KOL)

file.write("\nСлучайный массив:\n")
file.write("Проведено экспериментов: " + str(KOL) + "\n")
file.write("Размер массива: " + str(DIM) + "\n")
file.write("Сравнений: " + str(CTotal[0]/KOL) + " " + str(CTotal[1]/KOL) + " " + str(CTotal[2]/KOL) + "\n")
file.write("Перестановок: " + str(MTotal[0]/KOL) + " " + str(MTotal[1]/KOL) + " " + str(MTotal[2]/KOL))

file.close()
