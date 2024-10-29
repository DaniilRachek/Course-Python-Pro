def create_class(class_name: str, methods: dict) -> type:
    """
    Динамічно створює новий клас.
    :param class_name: Ім'я нового класу.
    :param methods: Словник з методами для класу.
    :return: Новий створений клас.
    """
    return type(class_name, (object, ), dict(methods))


def say_hello(self):
    return "Hello!"


def say_goodbye(self):
    return "Goodbye!"


if __name__ == "__main__":
    methods = {
        "say_hello": say_hello,
        "say_goodbye": say_goodbye
    }

    MyDynamicClass = create_class("MyDynamicClass", methods)

    obj = MyDynamicClass()
    print(obj.say_hello())  # Hello!
    print(obj.say_goodbye())  # Goodbye!
    print(type(obj))  # <class '__main__.MyDynamicClass'>
    print(type(MyDynamicClass))  # <class 'type'>

