# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

my_list = [random.randrange(1, 7, 1) for i in range(10)]
res_list = list()

for i in range(len(my_list)):
    if my_list.count(i) == 1:
        res_list.append(i)
print(my_list)
print(res_list)
