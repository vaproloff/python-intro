# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

# str_lst = ['blue', 'green', 'wh2te', 'red', 'gray']
# num = 2
# for str in str_lst:
#     for j in str:
#         if num == j:
#             print(True)
#             break

# str_lst = ['blue', 'green', 'wh23te', 'red', 'gray']
# num = 23
# for i in str_lst:
#     if str(num) in i:
#         print(True)
#         break

str_lst = ['blue', 'green', 'wh23te', 'red', 'gray']
num = 2
for i in str_lst:
    if i.count(str(num)):
        print(True)
        break
