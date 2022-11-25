# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
import math

# Способ 1: с библиотекой math и функцией math.factorial
# num = int(input('Введите число N: '))
# for i in range(1, num + 1):
#     print(math.factorial(i), end=' ')


# Способ 2: с накапливанием строки и рекурсивной функцией, вычисляющей факториал
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
# num = int(input('Введите число N: '))
# prod_str = ''
# for i in range(1, num + 1):
#     prod_str += f'{str(fact(i))} '
# print(prod_str)


# Способ 3: с массивом и накапливанием произведения
num = int(input('Введите число N: '))
prod_arr = []
if num > 0:
    prod_arr.append(1)
for i in range(1, num):
    prod_arr.append((i + 1) * prod_arr[i - 1])
print(prod_arr)
