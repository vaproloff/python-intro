# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
import math

x1 = float(input('Введите координату X точки 1: '))
y1 = float(input('Введите координату Y точки 1: '))
x2 = float(input('Введите координату X точки 2: '))
y2 = float(input('Введите координату Y точки 2: '))
distance = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
print('Длина отрезка между точками:', distance)

# Альтернативное решение со вводом координат точки через запятую
# a = input('Введите координаты точки А через запятую: ').split(',')
# b = input('Введите координаты точки B через запятую: ').split(',')
# distance = round(math.sqrt((float(b[0]) - float(a[0])) ** 2 + (float(b[1]) - float(a[1])) ** 2), 2)
# print('Длина отрезка между точками:', distance)
