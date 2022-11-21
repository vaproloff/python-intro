a = int(input('Введите a: '))
b = int(input('Введите b: '))

# print(a == b ** 2 or b == a ** 2)

if a == b ** 2:
    print(f'{a} является квадратом числа {b}')
elif b == a ** 2:
    print(f'{b} является квадратом числа {a}')
else:
    print('Нет квадратов')