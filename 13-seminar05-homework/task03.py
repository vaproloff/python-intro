# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def zip_data(data):
    zipped_str = ''
    prev_char = ''
    quantity = 1
    for cur_char in data:
        if cur_char == prev_char:
            quantity += 1
        else:
            if prev_char != '':
                zipped_str += str(quantity) + prev_char
            quantity = 1
            prev_char = cur_char
    zipped_str += str(quantity) + prev_char
    return zipped_str

def unzip_data(data):
    unzipped_str = ''
    quantity = ''
    for cur_char in data:
        if cur_char.isdigit():
            quantity += cur_char
        else:
            unzipped_str += cur_char * int(quantity)
            quantity = ''
    return unzipped_str

with open('task03-rawdata.txt', 'r') as file_data:
    raw_data = file_data.readline()
    print(f'Исходные данные: {raw_data}')

zipped_data = zip_data(raw_data)

with open('task03-zipped.txt', 'w') as file_data:
    file_data.write(zipped_data)
    print(f'Сжатые данные: {zipped_data}')

unzipped_data = unzip_data(zipped_data)

with open('task03-unzipped.txt', 'w') as file_data:
    file_data.write(unzipped_data)
    print(f'Восстановленные данные: {unzipped_data}')

print(f'Проверка исходных и восстановленных после сжатия данных: {raw_data == unzipped_data}')