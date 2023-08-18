# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random

min = int(input('Введите минимальное значение элемента \n'))
max = int(input('Введите максимальное значение элемент \n'))
n = int(input('Введите длину списка \n'))
rand_start = int(input('Ведите начала диапазона random \n'))
rand_end = int(input('Введите конец диапазона random \n'))


list = [random.randint(rand_start, rand_end) for i in range(n)]   # Генерация списка вариант 1
# list = [i for i in range(n)]                                     # Генерация списка вариант 2
list_res = []

def i_min_max(list):
    for i in range(n):
        if list[i] >=  min and list[i] <= max:
            list_res.append(i)
    return list_res

print(list)
print(i_min_max(list))

for i in range(len(list_res)):
    print(list[list_res[i]], end =", ")