import inspect
import math


def analyze_module(module: object) -> None:
    """
    Аналізує модуль та виводить класи та функції,
    які в ньому знаходяться.
    :param module: Модуль для аналізу
    """
    functions = inspect.getmembers(module, inspect.isfunction)
    builtin_functions = inspect.getmembers(module, inspect.isbuiltin)

    print("Функції:")
    for name, b_func in builtin_functions:
        try:
            sign = str(inspect.signature(b_func)).replace(", /", "")
        except ValueError:
            sign = "()"
        print(f'- {name}{sign}')
    for name, func in functions:
        try:
            sign = str(inspect.signature(func)).replace(", /", "")
        except ValueError:
            sign = "()"
        print(f'- {name}{sign}')
    print()

    classes = inspect.getmembers(module, inspect.isclass)
    print("Класи:")
    for name, cls in classes:
        print(f'- {name}{inspect.signature(cls)}')


if __name__ == "__main__":
    analyze_module(math)
