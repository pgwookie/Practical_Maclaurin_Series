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


def main():
    while True:
        print("Меню:")
        print("1. Вычислить sin(x)")
        print("2. Вычислить ln(1 - x)")
        print("3. Вычислить (1 + x)^m")
        print("4. Выход")

        choice = input("Введите номер функции (1-4): ")

        if choice == "4":
            print("Выход из программы.")
            break
        elif choice == "1":
            try:
                x = float(input("Введите значение x: "))
                print("sin(x) =", maclaurin_sin(x))
            except ValueError:
                print("Ошибка: Введите корректное значение x.")
        elif choice == "2":
            try:
                x = float(input("Введите значение x (|x| < 1): "))
                print("ln(1 - x) =", maclaurin_ln_1_minus_x(x))
            except ValueError as e:
                print("Ошибка:", e)
        elif choice == "3":
            try:
                x = float(input("Введите значение x (|x| < 1): "))
                m = float(input("Введите значение m: "))
                print("(1 + x)^m =", maclaurin_1_plus_x_pow_m(x, m))
            except ValueError as e:
                print("Ошибка:", e)
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
