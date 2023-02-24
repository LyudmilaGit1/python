"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

a = int(input("Введите порядковый номер месяца: "))
season = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(f"результат через список: {season[a - 1]}")


diction = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето',
           12: 'зима', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень'}

print(f"результат через словарь:{a} месяц - это {diction[a]}")