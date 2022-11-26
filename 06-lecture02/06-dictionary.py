dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary)
print(dictionary['left'])

for k in dictionary.keys():
    print(k)

for v in dictionary.values():
    print(v)

for e in dictionary:
    print(e)

for e in dictionary:
    print(dictionary[e])
