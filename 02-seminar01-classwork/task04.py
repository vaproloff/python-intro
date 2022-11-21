# num = float(input('Введите число: '))
# print(int((num % 1) * 10))

# num = input('Введите число: ')
# print(num.split('.')[1][0])

num = input('Введите число: ')
for i in range(len(num)):
    if num[i] == '.':
        print(num[i + 1])
        break