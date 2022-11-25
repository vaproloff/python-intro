# Задайте список из n чисел последовательности
# (1 + (1/n))^n и выведите на экран их сумму.

# Способ 1. Со словарём, как в примере
# n = int(input('Введите n: '))
# n_dict = {}
# val_sum = 0
# for i in range(1, n + 1):
#     val = round((1 + (1 / i)) ** i, 2)
#     n_dict[i] = val
#     val_sum += val
# print(f'Словарь последовательности: {n_dict}')
# print(f'Сумма последовательности: {val_sum}')


# Способ 2. Со списком, как указано в задании
n = int(input('Введите n: '))
n_list = []
val_sum = 0
for i in range(1, n + 1):
    val = round((1 + (1 / i)) ** i, 2)
    n_list.append(val)
    val_sum += val
print(f'Список последовательности: {n_list}')
print(f'Сумма последовательности: {val_sum}')
