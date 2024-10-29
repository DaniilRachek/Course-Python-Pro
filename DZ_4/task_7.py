def log_methods(cls: type) -> type:
    """
    Декоратор класу для логування методів класу.
    :param cls: Клас, який ми подаємо в декоратор.
    :return: Той же клас.
    """
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            setattr(cls, str(attr_name), log_method(attr_value))
    return cls


def log_method(method: object) -> object:
    """
    Декоратор методу, який логує метод.
    :param method: Метод класу.
    :return: Функція для логування.
    """
    def wrapper(*args, **kwargs):
        print(f"Logging: {method.__name__} called with {args[1:]}")
    return wrapper


@log_methods
class MyClass:
    """
    Клас для тестування декоратора @log_methods
    """
    def add(self, a: int, b: int) -> int:
        """
        Додає два числа.
        :param a: Перше число.
        :param b: Друге число.
        :return: Сума чисел.
        """
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """
        Віднімає друге число від першого.
        :param a: Перше число.
        :param b: Друге число.
        :return: Різниця чисел.
        """
        return a - b


if __name__ == "__main__":
    obj = MyClass()
    obj.add(5, 3)
    obj.subtract(5, 3)
