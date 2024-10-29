class Proxy:
    """
    Клас, який переадресовує виклики об'єктів,
    додатково логуючи їх.
    """
    def __init__(self, obj: object):
        """
        Ініціалізація класа.
        :param obj: Будь-який об'єкт.
        """
        self.obj = obj

    def __getattr__(self, item: str):
        """
        Переадресовує виклик методу об'єкта та логує його.
        :param item: Ім'я методу.
        :return: Метод, або атрибут об'єкта.
        """
        attr = getattr(self.obj, item)
        if callable(attr):
            def log_method(*args, **kwargs):
                print("Calling method:")
                print(f"{item} with args: {args, *kwargs}")
                return attr(*args)
            return log_method
        else:
            return attr


class MyClass:
    """
    Клас для тестування класу Proxy.
    """

    def greet(self, name: str) -> str:
        """
        Повертає рядок з привітанням і ім'ям
        :param name: Ім'я
        :return: Рядок з привітанням і ім'ям
        """
        return f"Hello, {name}!"


if __name__ == "__main__":
    obj = MyClass()
    proxy = Proxy(obj)

    print(proxy.greet("Alice"))
