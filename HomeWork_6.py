# Task1. Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# def Progression(a0, d, n):
#     a = [a0 + i * d for i in range(n)]
#     return a
#
# a0 = int(input("Введите первый элемент: "))
# d = int(input("Введите разность рядом стоящих элементов: "))
# n = int(input("Введите количество элементов: "))
#
# print(Progression(a0, d, n))


# Task2. Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# def Index(list, min, max):
#     list_1 = []
#     for i in range(len(list)):
#         if list[i] >= min and list[i] <= max:
#             list_1.append(i)
#     return list_1
#
# min = int(input("Введите минимальное число: "))
# max = int(input("Введите максимальное число: "))
#
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#
# print(Index(list_1, min, max))