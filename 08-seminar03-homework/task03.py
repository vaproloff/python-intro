# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.

float_lst = [1.1, 1.2, 3.1, 5, 10.05]
max_frac = 0
min_frac = 1
for i in float_lst:
    if type(i) == float:
        frac = i % 1
        if max_frac < frac:
            max_frac = frac
        if min_frac > frac:
            min_frac = frac
print(round(max_frac - min_frac, 3))
