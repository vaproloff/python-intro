# data = [x for x in range(10)]

# res = filter(lambda x: x % 2 == 0, data)
# print(res)

# res = list(filter(lambda x: not x % 2, data))
# print(res)



data = '1 2 3 4 5 6 7 8 9 10'.split()
res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)