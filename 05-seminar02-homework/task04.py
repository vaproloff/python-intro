# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = abs(int(input('Введите n: ')))
n_list = []
for i in range(-n, n + 1):
    n_list.append(i)
print(f'Список элементов: {n_list}')

pos_arr = []
file_path = 'file.txt'
pos_file = open(file_path, 'r')
for pos_line in pos_file:
    pos_arr.append(int(pos_line))
pos_file.close()
print(f'Список позиций из файла {file_path}: {pos_arr}')

sel_prod = 1
found_pos_arr = []
for i in pos_arr:
    if 0 <= i < len(n_list):
        found_pos_arr.append(i)
        sel_prod *= n_list[i]
    else:
        print(f'Позиции {i} не существует в списке элементов от {-n} до {n}')
print(f'Произведение найденных элементов на позициях {found_pos_arr}: {sel_prod}')
