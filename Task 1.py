# Вычислить число c заданной точностью d

import math


def truncate(number: float, digits: int):
    pow10 = 10 ** digits
    return number * pow10 // 1 / pow10


precision = int(input("Введите количество знаков после запятой: "))
res_pi = truncate(math.pi, precision)
print(f"Число ПИ с точнойстью {precision} знака равно {res_pi}")
