# Написать программу сложения двух чисел

num_sum = lambda a, b: a + b

x = int(input('x = '))
y = int(input('y = '))
print(f'{x} + {y} = {num_sum(x, y)}')