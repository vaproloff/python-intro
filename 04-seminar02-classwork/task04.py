# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

# num = input('Введите число: ').replace('.', '').replace(',', '')
# sum = 0
# for i in range(len(num)):
#     sum += int(num[i])
# print(sum)

num = float(input('Введите число: '))
while num % 1 > 0:
    num *= 10
sum = 0
while num > 0:
    rem = num % 10
    sum += rem
    num //= 10
print(int(sum))
