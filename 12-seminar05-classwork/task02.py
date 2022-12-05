# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие
# A[i] - 1 = A[i-1]. Найдите это число.

with open('task02-file.txt', 'r') as data:
    num_str = data.readline()

num_lst = list(map(int, num_str.split()))
print(num_lst)

for i in range(1, len(num_lst)):
    if num_lst[i] - num_lst[i - 1] != 1:
        num_lst.insert(i, num_lst[i - 1] + 1)
print(num_lst)

with open('task02-file.txt', 'w') as data:
    data.write(' '.join(map(str, num_lst)))