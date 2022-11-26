# Запись данных в файл
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors)
# data.write('\nLINE2\n')
# data.write('LINE3\n')
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')


# Чтение данных из файла
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
