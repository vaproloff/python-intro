# a = 123
# b = 1.23
# print(a)
# # print(type(a))
# print(b)
# s = 'hello world'
# print(s)

# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print('{2} - {0} - {1}'.format(b, s, a))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# Списки
# list = [1,2,3]
# print(list)

# list = ['1', '2', '3', 'hello world', 1,2,3, True]
# print(list)

#---------------------------
# Ввод и вывод данных
# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, b)
# print(a, '+', b, '=', a + b)

# print('Введите a')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, b)
# print(a, '+', b, '=', a + b)

#---------------------------
# Арифметические операции
# a = 123
# b = 321
# c = a + b
# print(c)

# a = 123
# b = -321 # Унарный минус
# c = a + b
# print(c)

# a = 2
# b = 8
# c = a / b
# print(c)

# a = 12
# b = 8
# c = a // b # Целочисленное деление
# print(c)

# a = 12
# b = 8
# c = a % b # Остаток от деления
# print(c)

# a = 2
# b = 8
# c = a ** b # Возведение в степень
# print(c)

# a = 1.3
# b = 3
# c = a * b # Умножение
# print(c)

# a = 1.3
# b = 3
# c = round(a * b, 1) # Округление
# print(c)

#---------------------------
# Логические операции
# a = 1 > 3
# print(a)

# a = 1 < 3 and 5 > 2
# print(a)

# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1, 2]
# b = [1,2]
# print(a == b)

# a = 1 < 3 < 5
# print(a)

# func = 1
# T = 4
# x = 123
# print(func<T>(x))

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f)

# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)

# is_odd = f[0] % 2 == 0
# print(is_odd)
# is_odd = not f[0] % 2
# print(is_odd)

#---------------------------
# Условные конструкции
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет,', username)

#---------------------------
# Цикл while
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('Хватит )')
# print(inverted)

#---------------------------
# Цикл for
# for i in 1,2,3,4,5:
#     print(i ** 2)

# list = [1,2,4,64,4,10]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(2, 10):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in 'qwerty':
#     print(i)

#---------------------------
# Работа со строками
# text = 'съешь ещё этих мягких французских булок'
# print(len(text))
# print('ещё' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('ещё', 'ЕЩЁ'))

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])
# print(text[1])
# # print(text[len(text)])
# print(text[len(text) - 1])
# print(text[-5])
# print(text[:])
# print(text[:2])
# print(text[2:5])
# print(text[6:-18])
# print(text[0:len(text):6])
# print(text[::6])
# text = text[2:9] + text[-5] + text[:2]
# print(text)

#---------------------------
# Списки
# numbers = [1,2,3,4,5]
# print(numbers)
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# print(numbers)
# numbers[0] = 10
# print(f'{len(numbers)}')

# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)

# for e in colors:
#     print(e * 2)

# colors.append('gray') # Добавить элемент в конец
# print(colors == ['red', 'green', 'blue', 'gray'])
# colors.remove('red') # Удалить элемент
# print(colors)
# del colors[0]
# print(colors)

#---------------------------
# Функции
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(type(f(arg)))