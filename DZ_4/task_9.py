class DynamicProperties:
    """
    Клас для динамічного додавання властивостей.
    """
    def __init__(self):
        """
        Ініціалізація класу.
        _values - словник з імена і значеннями властивостей,
        які додаємо.
        """
        self._values = {}

    def add_property(self, name, value):
        """
        Метод для динамічного додавання властивостей до класу.
        :param name: Ім'я нового атрибуту чи методу.
        :param value: Значення нового атрибуту чи методу.
        """

        def getter():
            return self._values.get(name)

        def setter():
            self._values[name] = value

        prop = property(getter, setter)
        setattr(self, name, value)


def say_hello():
    return "Hello!"


def say_hello2():
    return "Hello!!"


if __name__ == "__main__":
    obj = DynamicProperties()
    obj.add_property('name', 'default_name')
    print(obj.name)  # default_name
    obj.name = "Python"
    print(obj.name)  # Python

    obj.add_property('age', '12')
    print(obj.age)  # 12
    obj.age = 13
    print(obj.age)  # 13

    obj.add_property('hello', say_hello())
    print(obj.hello)  # Hello!

