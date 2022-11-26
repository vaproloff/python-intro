def concatenation(*params):
    res: int = 0
    for item in params:
        res += item
    return res


# print(concatenation('a', 's', 'd', 'w'))
# print(concatenation('a', '1'))
print(concatenation(1, 2, 3, 4))
