# lst = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         lst.append(i)
#
# print(lst)

# lst = [i for i in range(1, 21)]
# lst = [i for i in range(1, 21) if i % 2 == 0]
# lst = [(i, i) for i in range(1, 21) if i % 2 == 0]
# print(lst)

# def f(x):
#     return x ** 3

# lst = [f(i) for i in range(1, 21) if i % 2 == 0]

# lst = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(lst)



# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# with open('file.txt', 'r') as nums:
#     pairs = [(int(i), (lambda i: i ** 2)(int(i))) for i in nums if int(i) % 2 == 0]
#     print(pairs)


# f = open('file2.txt', 'r')
# data = f.read() + ' '
# f.close()
#
# numbers = []
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
#
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)


def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 4 5 6 7 8 9 10'.split()
res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x ** 2), res)
print(res)
