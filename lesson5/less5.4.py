"""Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!"""

def summ(num, b=1, sum=0):
    if num == 0:
        return float(sum)
    if num > 0:
        sum = sum + b
    return summ(num - 1, b / -2, sum)

a = int(input('Введите ваше число:'))
print(f'Колличество элементов - {a}, их сумма: {summ(a)}')

