# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


num = int(input("Введите целое число: "))
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return factors


num = int(input("Введите число: "))

nums = factorize(num)
print(f"Простыми множителями числа {num} являются числа {nums}")
