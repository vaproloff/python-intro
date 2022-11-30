# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Вариант с готовым списком и циклом for
# num_lst = [2, 3, 4, 5, 6, 7, 2]
# pair_lst = []
# for i in range(int((len(num_lst) + 1) / 2)):
#     pair_lst.append(num_lst[i] * num_lst[-i - 1])
# print(pair_lst)


# Вариант с заданием списка и циклом while
num_lst = input('Введите числа через запятую: ').split(',')
pair_lst = []
i = 0
while i < (len(num_lst) - i):
    pair_lst.append(int(num_lst[i]) * int(num_lst[-i - 1]))
    i += 1
print(pair_lst)
