def analyze_inheritance(cls: type):
    """
    Аналізує даний клас і виводить усі методи,
    які успадковує цей клас від базових класів окрім object.
    :param cls: Клас, який треба проаналізувати.
    """
    parents = cls.__mro__[1:-1]
    if parents:
        print(f'Клас {cls.__name__} наслідує:')
        for parent in parents:
            for attr_name, attr_value in parent.__dict__.items():
                if not attr_name.startswith("__"):
                    print(f'- {attr_name} з {parent.__name__}')
    else:
        print(f'Клас {cls.__name__} не наслідує жодних методів.')


class GrandParent:
    """
    Базовий клас, від якого будуть успадковуватись
    інші класи.
    """
    def grandparent_method(self):
        pass


class Parent(GrandParent):
    """
    Клас, який успадковує методи від класу GrandParent,
    та від якого буде успадковуватись нижчий клас.
    """
    def parent_method(self):
        pass


class Child(Parent):
    """
    Найнижчий клас, який успадковує методи від класу Parent.
    """
    def child_method(self):
        pass


class Product:
    """
    Клас, який нічого не успадковує.
    """
    pass


if __name__ == "__main__":
    analyze_inheritance(Child)
    print()
    analyze_inheritance(Product)