# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

def parse_expression(exp):
    exp = exp.replace(' ', '').replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ').split()
    return exp

def my_eval(exp):
    i = 0
    while '*' in exp or '/' in exp:
        if exp[i] == '*' or exp[i] == '/':
            if exp[i] == '*':
                exp[i - 1] = float(exp[i - 1]) * float(exp[i + 1])
            else:
                exp[i - 1] = float(exp[i - 1]) / float(exp[i + 1])
            exp.pop(i)
            exp.pop(i)
            i -= 2
        i += 1
    j = 0
    while '+' in exp or '-' in exp:
        if exp[j] == '+' or exp[j] == '-':
            if exp[j] == '+':
                exp[j - 1] = float(exp[j - 1]) + float(exp[j + 1])
            else:
                exp[j - 1] = float(exp[j - 1]) - float(exp[j + 1])
            exp.pop(j)
            exp.pop(j)
            j -= 2
        j += 1
    return exp[0]

# expression = input('Введите арифметическое выражение')
expression = '1* 2 + 13 /5-20 * 3.35 / 2'
print(f'Результат функции eval: {eval(expression)}')
print(f'Результат нашей функции: {my_eval(parse_expression(expression))}')
