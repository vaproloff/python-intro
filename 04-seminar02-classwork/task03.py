# Напишите программу, в которой пользователь будет задавать
# две строки, а программа - определять количество вхождений одной строки в другой.

str1 = input('Введите первую строчку: ').lower()
str2 = input('Введите вторую строчку: ').lower()

# str1_arr = str1.split()
# count = 0
# for i in str1_arr:
#     if i.lower() == str2.lower():
#         count += 1
print(str1.count(str2))

# str1_arr = str1.split()
# str2_arr = str2.split()
# count = 0
# for i in str1_arr:
#     for j in str2_arr:
#         if i.lower() == j.lower():
#             count += 1
# print(count)
