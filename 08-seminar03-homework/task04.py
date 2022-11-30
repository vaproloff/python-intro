# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


# Обычный метод с циклом while
def dec_to_bin(num):
    bin_num = ''
    while num > 0:
        bin_num = f'{num % 2}{bin_num}'
        num = num // 2
    return bin_num


# Рекурсивный метод и тернарное выражение
def dec_to_bin_rec(num):
    # if num == 0:
    #     return ''
    # else:
    #     return f'{dec_to_bin_rec(num // 2)}{num % 2}'
    return f'{dec_to_bin_rec(num // 2)}{num % 2}' if num > 0 else ''


dec_num = int(input('Введите число: '))
print(dec_to_bin(dec_num))
print(dec_to_bin_rec(dec_num))
