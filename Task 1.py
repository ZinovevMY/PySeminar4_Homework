# Вычислить число c заданной точностью d

import math


precision = int(input("Введите количество знаков после запятой: "))
pow10 = 10 ** precision
res_pi = lambda x: x * pow10 // 1 / pow10
print(f"Число ПИ с точнойстью {precision} знака равно {res_pi(math.pi)}")
