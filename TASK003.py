"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
a = input("Введите число: ")
b = a+a
c = a+a+a
d = int(a) + int(b) + int(c)
print(f"{a} + {b} + {c} = {d}")
