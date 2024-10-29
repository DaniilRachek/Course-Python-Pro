class MyClass:
    """
    Клас для перевірки функції analyze_object

    Атрибути:
        value (str): Ім'я
    """
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"

    def say_bye(self):
        return f"Goodbye, {self.value}"


def analyze_object(obj: object):
    """
    Виводить тип заданого об'єкта, його аргументи, методи та їх типи.
    :param obj : Будь-який об'єкт
    """
    print(f"Тип об'єкта: {type(obj)}")
    print("Атрибути і Методи:")
    for i in dir(obj)[::-1]:
        if i.startswith("__"):
            continue
        else:
            attr_value = getattr(obj, i)
            print(f"- {i}: {type(attr_value)}")


if __name__ == "__main__":
    my_obj = MyClass("Max")
    analyze_object(my_obj)
