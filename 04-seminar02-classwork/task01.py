# Напишите программу, которая принимает на вход
# число N и выдаёт последовательность из N членов.

# num = int(input('Введите число N: '))
# arr = [1]
# for i in range(1, num):
#     arr.append(arr[i - 1] * -3)
# print(arr)

num = int(input('Введите число N: '))
a = 1
for i in range(num):
    print(a, end=' ')
    a *= (-3)
