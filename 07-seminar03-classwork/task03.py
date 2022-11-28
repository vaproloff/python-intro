# Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.

lst = ["123", "234", 123, "567"]
elem = '123'
count = 0
index = -1
for i in range(len(lst)):
    if elem == lst[i]:
        count += 1
    if count == 2:
        index = i
        break
print(index)
