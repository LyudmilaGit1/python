"""Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""




a = (int(input("Введите первый элемент")))
b = (int(input("Введите количество элементов")))
c = (int(input("Введите разность элементов")))
r = range(a, b * c, c)
for i in r:
    print(i, end=',')


