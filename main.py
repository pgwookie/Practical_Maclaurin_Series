import math


def maclaurin_sin(x, n=10):
    """
    Вычисление sin(x) через ряд Маклорена
    """
    result = 0
    for k in range(n):
        result += ((-1)**k * x**(2*k + 1)) / math.factorial(2*k + 1)
    return result
