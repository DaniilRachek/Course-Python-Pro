from typing import Any


class MutableClass:
    """
    Клас з методами для динамічного додавання та видалення атрибутів.
    """
    def add_attribute(self, name: str, value: Any) -> None:
        """
        Додає новий атрибут до класу.
        :param name: Ім'я нового атрибута.
        :param value: Значення нового атрибута
        """
        if not getattr(self, name, None):
            self.__setattr__(name, value)
        else:
            print("Атрибут з даним ім'ям вже існує.")

    def remove_attribute(self, name: str) -> None:
        """
        Видаляє атрибут з класу.
        :param name: Ім'я атрибута, який хочемо видалити.
        """
        if getattr(self, name, None):
            self.__delattr__(name)
        else:
            print("Атрибуту з даним ім'ям не існує.")


if __name__ == "__main__":
    obj = MutableClass()

    obj.add_attribute("name", "Python")
    print(obj.name)  # Python
    obj.add_attribute("name", "C#")  # Атрибут з даним ім'ям вже існує.

    obj.remove_attribute("name")
    obj.remove_attribute("name")  # Атрибуту з даним ім'ям не існує.
    print(obj.name)  # Виникне помилка, атрибут видалений
