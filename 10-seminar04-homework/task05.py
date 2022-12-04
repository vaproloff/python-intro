# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*
# *Доп задание: для разного размера уравнения

def purify_poly(poly):
    poly = poly[:str.index(poly, '=') - 1]
    poly = poly.replace('- ', '-').replace('+ ', '+').split()
    for i in range(len(poly)):
        if '*' in poly[i]:
            poly[i] = poly[i].split('*')
            poly[i][1] = poly[i][1].replace('x^', '').replace('x', '1')
        else:
            poly[i] = poly[i].split('*')
            poly[i].append('0')
        poly[i] = (int(poly[i][0]), int(poly[i][1]))
    return poly

def sum_poly(p1, p2):
    p_sum = p1 + p2
    p_sum.sort(key=lambda k: k[1], reverse=True)
    i = 1
    while i < len(p_sum):
        if p_sum[i][1] == p_sum[i - 1][1]:
            p_sum[i - 1] = (p_sum[i - 1][0] + p_sum[i][0], p_sum[i - 1][1])
            p_sum.pop(i)
        i += 1
    return p_sum

def stringify_poly(poly):
    poly_lst = []
    for i in poly:
        if i[0] != 0:
            if abs(i[0]) == 1:
                coef = f'{"+" if i[0] > 0 else "-"}{" " if i[1] != 0 else " 1"}'
            else:
                coef = f'+ {i[0]}' if i[0] > 0 else f"- {-i[0]}"
            x = "" if i[1] == 0 else f'{"" if abs(i[0]) == 1 else "*"}x{"" if i[1] == 1 else f"^{i[1]}"}'
            poly_lst.append(coef + x)
    poly_lst[0] = poly_lst[0].replace('+ ', '').replace('- ', '-')
    return str.join(' ', poly_lst) + ' = 0'

with open('poly1.txt', 'r') as data1:
    poly1 = data1.readline()
    # print(poly1)
with open('poly2.txt', 'r') as data2:
    poly2 = data2.readline()
    # print(poly2)
with open('sum-poly.txt', 'w') as data_sum:
    poly_sum = stringify_poly(sum_poly(purify_poly(poly1), purify_poly(poly2)))
    data_sum.write(poly_sum)
    # print(poly_sum)
