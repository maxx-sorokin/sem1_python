"""
a = int(input('Введите А: '))

b = input('Введите B: ')
b = int(b)
c = a + b
print(c)
print(type(c))

a = 6
b = 8
if a >b:
    print(a)
elif a==b:
    print('равны')
else:
    print(b)
"""


"""
Задача 1. За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.

import math
n = int(input('Введите n: '))
m = int(input('Введите m: '))

d = m / n

print(math.ceil(d))
"""
"""
n = int(input('Введите n: '))
m = int(input('Введите m: '))

d = (m + n - 1) // n

print(d)
"""

n = int(input('Скорость в день: '))
m = int(input('Расстояние км: '))

t = m//n
ostatok = (m % n) > 0
ostatokBool = bool(ostatok)
ostatokDays = int(ostatok)

print('Дней ', t + ostatokDays)
