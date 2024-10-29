class Calculator:
    """
    Клас калькулятора для тестування функції call_function()

    """
    def add(self, a: int, b: int) -> int:
        """
        Додає два числа

        :param a: Перше число.
        :param b: Друге число
        :return: Сума двох чисел
        """
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """
        Віднімає одне число від другого

        :param a: Перше число.
        :param b: Друге число
        :return: Різниця двох чисел
        """
        return a - b


def call_function(obj: object, method_name: str, *args) -> object:
    """
    Функція, яка динамічно викликає метод об'єкта.
    :param obj: Будь-який об'єкт.
    :param method_name: Назва методу об'єкта.
    :param args: Аргументи, які передаємо методу.
    :return: Результат виконання метода.
    """
    method = getattr(obj, method_name)
    return method(*args)


if __name__ == "__main__":
    calc = Calculator()
    print(call_function(calc, "add", 10, 15))
    print(call_function(calc, "subtract", 15, 10))
