# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

n = int(input('Введите N: '))
fibo = [0]
if n > 0:
    fibo.append(1)
    fibo.insert(0, 1)
for i in range(3, n * 2 + 1, 2):
    fibo.append(fibo[i - 2] + fibo[i - 1])
    fibo.insert(0, fibo[1] - fibo[0])
print(fibo)
