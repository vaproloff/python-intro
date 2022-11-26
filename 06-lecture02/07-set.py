# colors = {'red', 'green', 'blue'}
#
# print(colors)
# print(type(colors))
#
# colors.add('red')
# print(colors)
#
# colors.add('gray')
# print(colors)
#
# colors.remove('red')
# print(colors)
#
# # colors.remove('red')
# colors.discard('red')
# print(colors)
#
# colors.clear()
# print(colors)


a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

c = a.copy()
print(c)

u = a.union(b)
print(u)

i = a.intersection(b)
print(i)

dl = a.difference(b)
print(dl)

dr = b.difference(a)
print(dr)

q = a \
    .union(b) \
    .difference(a.intersection(b))
print(q)

s = frozenset(a)