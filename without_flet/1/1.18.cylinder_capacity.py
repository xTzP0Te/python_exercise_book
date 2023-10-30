# Объем цилиндра может быть рассчитан путем умножения площади круга,
# лежащего в его основе, на высоту. Напишите программу, в которой поль-
# зователь будет задавать радиус цилиндра и его высоту, а в ответ получать
# его объем, округленный до одного знака после запятой.


import math

r = float(input("Введите радиус цилиндра: "))
h = float(input("Введите высоту цилиндра: "))

V = math.pi * r**2 * h

print(f"Объем цилиндра: {V:.1f}")
