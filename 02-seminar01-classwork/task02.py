numbers = [1, 4, 5, 6, 8]
max = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
print('Максимальное число:', max)