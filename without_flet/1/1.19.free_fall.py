# Напишите программу для расчета скорости объекта во время его сопри-
# косновения с землей. Пользователь должен задать высоту в метрах, с ко-
# торой объект будет отпущен. Поскольку объекту не будет придаваться
# ускорение, примем его начальную скорость за 0 м/с. Предположим, что
# ускорение свободного падения равно 9,8 м/с2. При известных начальной
# скорости (vi), ускорении (a) и дистанции (d) можно вычислить скорость
# при соприкосновении объекта с землей по формуле vf = sqrt(vi**2+2*a*D)


import math

vi = 0
g = 9.8

D = float(input("Введите высоту в метрах, с которой объект будет отпущен: "))

vf = math.sqrt(vi**2 + 2*g*D)

print(f"Скорость объекта при соприкосновении с землей составит: {vf:.2f} м/с")