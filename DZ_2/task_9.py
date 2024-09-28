from math import factorial


def memoize(function):
    """Декоратор для кешування результатів функції"""
    cache = {}

    def memoize_func(value):
        if value in cache:
            print(f"Кешоване значення для {value}: {cache[value]}")
            return cache[value]
        else:
            cache[value] = function(value)
            return cache[value]
    return memoize_func


@memoize
def memoize_factorial(value):
    """Функція для обчислення факторіала"""

    result = factorial(value)
    print(f"Обчислене значення факторіала {value}: {result}")
    return result


memoized = memoize_factorial

memoized(7)
memoized(8)
memoized(7)
