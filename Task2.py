# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
min = int(input("min = "))
max = int(input("max = "))
N = int(input("N = "))
arr_index = []
arr = [random.randint(1,99) for _ in range(N)]
print(arr)
for i in arr:
    if max > i and i > min:
        arr_index.append(arr.index(i))
print(arr_index)