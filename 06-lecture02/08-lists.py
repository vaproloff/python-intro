# list1 = [1, 2, 3, 4, 5]
# list2 = list1
#
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)
#
# list1[0] = 123
# list2[1] = 234
# print()
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)


list1 = [1, 2, 3, 4, 5]

print(list1.pop())
print(list1)
print(list1.pop(2))
print(list1)
list1.insert(2, 11)
print(list1)
list1.append(11)
print(list1)
