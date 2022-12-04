# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

# Способ 1. Со количественным словарём
# nums = input('Введите список чисел через запятую: ').split(',')
# nums_quantities = {}
# for num in nums:
#     nums_quantities[num] = nums_quantities[num] + 1 if nums_quantities.get(num) else 1
# nums_unique = [int(i) for i in nums if nums_quantities[i] == 1]
# print(f'Список уникальных чисел: {nums_unique}')


# Способ 2. С map, filter
nums_input = input('Введите список чисел через запятую: ')
nums = list(map(lambda num: int(num), nums_input.split(',')))
print(f'Исходный список чисел: {nums}')

nums_quantities = map(lambda num: (num, nums.count(num)), nums)
nums_quantities_unique = filter(lambda num: num[1] == 1, nums_quantities)
nums_unique = list(map(lambda num: num[0], nums_quantities_unique))
print(f'Список уникальных чисел: {nums_unique}')
