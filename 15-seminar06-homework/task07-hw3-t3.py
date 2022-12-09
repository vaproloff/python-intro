# ДЗ. Семинар 3. Задача 3
# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.

float_lst = [1.1, 1.2, 3.1, 5, 10.05]
frac_lst = list(map(lambda i: i % 1, filter(lambda i: type(i) == float, float_lst)))
print(round(max(frac_lst) - min(frac_lst), 3))