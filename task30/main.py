# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input('Введите первый элемент \n'))
d = int(input('Введите разность между элементами \n'))
n = int(input('Введите количество элементов \n'))

#  ВАРИАНТ 1:

# an = [a]
# def aref_progr(a, d, n):

#     for i in range(n-1):
#         x = a + d
#         an.append(x)
#         a += d
#     return an

# print(f'Вариант 1: {aref_progr(a, d, n)}')

# ВАРИАНТ 2

# an = []
# def aref_progr_2(a, d, n):
#     for i in range(n):
#         x = (a + i * d)
#         an.append(x)
#     return an
# print(f'Вариант 2: {aref_progr_2(a, d, n)}')

# ВАРИАНТ 3

for i in range(n):
    print(a + i *d, end =' ')