class SingletonMeta(type):
    """
    Мета-клас SingletonMeta, який забезпечує реалізацію патерну Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Реалізація методу __call__, який створює або повертає існуючий екземпляр класу.
        :param cls: Клас, для якого виконується виклик.
        :param args: Додаткові позиційні аргументи для ініціалізації екземпляра.
        :param kwargs: Додаткові іменовані аргументи для ініціалізації екземпляра.
        :return: Існуючий або новостворений екземпляр класу.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    Клас Singleton, який використовує мета-клас SingletonMeta для реалізації патерну Singleton.
    """
    def __init__(self):
        """
        Ініціалізує екземпляр класу Singleton і виводить повідомлення про створення екземпляра.
        """
        print("Creating instance")


if __name__ == "__main__":
    obj1 = Singleton()  # Creating instance
    obj2 = Singleton()
    print(obj1 is obj2)  # True

