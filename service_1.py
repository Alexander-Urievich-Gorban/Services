"""Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):"""


def get_resolution(a, b, c):
    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)
    if discr > 0:
        import math

        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("Корней нет")
