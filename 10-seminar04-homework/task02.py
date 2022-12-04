# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N

n = int(input('Введите натуральное число N: '))

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def decompose_num(num):
    prime_muls = []
    while not is_prime(num):
        for i in range(2, num + 1):
            if is_prime(i) and num % i == 0:
                prime_muls.append(i)
                num = int(num / i)
                break
    else:
        prime_muls.append(num)
    return " * ".join(map(str, prime_muls))

print(f'Список множителей числа {n}: {decompose_num(n)}')
