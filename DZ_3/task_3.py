class Person:
    """
    Клас для представлення людини.

    Атрибути:
        name (str) : Ім'я людини.
        age (int) : Вік людини.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        """
        Перевіряє чи вік першої людини менший за вік другої.

        Аргументи:
            other (Person) : Друга людина, з якою порівнюємо.

        Повертає:
            bool: Більше чи менше вік першої людини.
        """
        return self.age < other.age

    def __eq__(self, other):
        """
        Перевіряє чи вік першої людини дорівнює віку другої.

        Аргументи:
            other (Person) : Друга людина, з якою порівнюємо.

        Повертає:
            bool: Чи дорівнює вік двох людей.
        """
        return self.age == other.age

    def __gt__(self, other):
        """
        Перевіряє чи вік першої людини більший за вік другої.

        Аргументи:
            other (Person) : Друга людина, з якою порівнюємо.

        Повертає:
            bool: Більше чи менше вік першої людини.
        """
        return self.age > other.age

    def __repr__(self):
        """
        Повертає строкове представлення людини.

        Повертає:
            str : Строкове представлення в форматі 'ім'я, вік'.
        """
        return f"{self.name}, {self.age}."


def sort_by_age(list_of_people: list) -> list:
    """
    Сортує список людей за зростанням по віку

    Аргументи:
        list_of_people (list) : Невідсортований список людей.

    Повертає:
        list : Відсортований список за віком.
    """
    if len(list_of_people) <= 1:
        return list_of_people
    else:
        elem = list_of_people[len(list_of_people) // 2].age
        left = [x for x in list_of_people if x.age < elem]
        middle = [x for x in list_of_people if x.age == elem]
        right = [x for x in list_of_people if x.age > elem]
        return sort_by_age(left) + middle + sort_by_age(right)


people = [Person("Ivan", 14), Person("Denys", 42), Person("Yaroslav", 31), Person("Mariya", 30)]
print(*sort_by_age(people))
print(*sorted(people, key=lambda x: x.age))

