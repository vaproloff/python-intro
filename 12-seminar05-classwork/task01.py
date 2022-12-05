# Посчитать НОК и НОД числа

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

list_of_factor = []
list_of_factor_2 = []

def f(n, list):
    num_factor = 2
    while n > 1:
        if n % num_factor == 0:
            list.append(num_factor)
            n = int(n / num_factor)
        else:
            num_factor += 1

f(num1, list_of_factor)
f(num2, list_of_factor_2)

nod_find = set(list_of_factor).intersection(set(list_of_factor_2))
nod = 1
for i in nod_find:
    nod = nod * i
print(nod)

nok = num1 * num2 / nod
print(nok)

