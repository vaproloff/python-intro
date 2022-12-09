# ДЗ. Семинар 2. Задача 4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import math

n = abs(int(input('Введите n: ')))
n_list = [i for i in range(-n, n + 1)]
print(f'Список элементов: {n_list}')

with open('file.txt', 'r') as pos_file:
    pos_arr = [int(i) for i in pos_file]
print(f'Список позиций из файла: {pos_arr}')

prod = math.prod(map(lambda i: n_list[i], filter(lambda i: 0 <= i < len(n_list), pos_arr)))
print(f'Произведение найденных элементов: {prod}')
