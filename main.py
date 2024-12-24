import math


def maclaurin_sin(x, n=10):
    """
    Вычисление sin(x) через ряд Маклорена
    """
    result = 0
    for k in range(n):
        result += ((-1)**k * x**(2*k + 1)) / math.factorial(2*k + 1)
    return result


def maclaurin_ln_1_minus_x(x, n=10):
    """
    Вычисление ln(1 - x) через ряд Маклорена
    """
    if abs(x) >= 1:
        raise ValueError("Значение x должно быть в диапазоне |x| < 1.")
    result = 0
    for k in range(1, n + 1):
        result -= x**k / k
    return result


def maclaurin_1_plus_x_pow_m(x, m, n=10):
    """
    Вычисление (1 + x)^m через разложение в ряд Маклорена.
    """
    if abs(x) >= 1:
        raise ValueError("Значение x должно быть в диапазоне |x| < 1.")
    result = 1  # Первое слагаемое
    term = 1  # Для вычисления каждого следующего члена ряда
    for k in range(1, n):
        term *= (m - (k - 1)) * x / k
        result += term
    return result


