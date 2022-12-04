# Вычислить число Пи c заданной точностью d
import math

d = float(input('Задайте точность: '))

# Вариант 1
print(int(math.pi * (1 / d)) * d)

# Вариант 2
print(str(math.pi)[0:len(str(d))])
