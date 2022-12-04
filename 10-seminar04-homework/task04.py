# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100)* многочлена и записать в файл многочлен степени k.
# *Доп задание: значения коэффициентов от -100 до 100
from random import randint

def make_term(term_raw):
    if term_raw[0] == 0:
        return ''
    else:
        if term_raw[0] < 0:
            if term_raw[0] == -1:
                term = '- 1' if term_raw[1] == '' else '- '
            else:
                term = f'- {-term_raw[0]}'
                if term_raw[1] != '':
                    term += '*'
        else:
            if term_raw[0] == 1:
                term = '+ 1' if term_raw[1] == '' else '+ '
            else:
                term = f'+ {term_raw[0]}'
                if term_raw[1] != '':
                    term += '*'
        if term_raw[1] != '':
            term += f'{term_raw[1]}'
        return term

k = int(input('Введите k: '))
coefs = [randint(-100, 100) for i in range(k + 1)]
terms = [f'x^{i}' for i in range(k, 1, -1)]
terms.append('x')
terms.append('')
terms = zip(coefs, terms)
terms = list(map(make_term, terms))
terms[0] = terms[0].replace('+ ', '').replace('- ', '-')
polynomial = str.join(' ', terms) + ' = 0'
# print(polynomial)
with open('file.txt', 'w') as data:
    data.write(polynomial)