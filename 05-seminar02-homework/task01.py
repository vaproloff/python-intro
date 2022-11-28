# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр. (Сделать для строки)

num_input = input('Введите число: ')
num = num_input.replace('.', '').replace(',', '')
sum_digits = 0
for i in range(len(num)):
    sum_digits += int(num[i])
print(f'Сумма цифр числа {num_input}: {sum_digits}')

# num_input = input('Введите число: ')
# sum_digits = 0
# for i in num_input:
#     if i.isdigit():
#         sum_digits += int(i)
# print(f'Сумма цифр числа {num_input}: {sum_digits}')
