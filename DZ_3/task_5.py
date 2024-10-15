class List:
    """
    Клас для представлення списку

    Атрибути:
        items (tuple): Кортеж елементів списку, переданих під час ініціалізації.
    """

    def __init__(self, *args):
        self.items = args

    def __len__(self):
        """
        Повертає кількість елементів у списку.

        Повертає:
            int: Кількість елементів у списку.
        """
        return len(self.items)

    def __iter__(self):
        """
        Повертає ітератор для елементів списку.

        Повертає:
            iterator: Ітератор для доступу до елементів списку.
        """
        return iter(self.items)

    def __getitem__(self, index):
        """
        Повертає значення елементу у списку за індексом.

        Аргументи:
            index (int): Індекс елементу у списку.

        Повертає:
            object: Елемент списку за заданим індексом.
        """
        return self.items[index]


def my_len(arr: List) -> int:
    """
    Функція для отримання довжини списку.

    Атрибути:
        arr (List): Створенний список.

    Повертає:
        int: Довжина списку.
    """
    return arr.__len__()


def my_sum(arr: List) -> int:
    """
    Функція для розрахування суми елементів списку.

    Аргументи:
        arr (List): Створенний список.

    Повертає:
        total (int): Загальна сума елементів списку.
    """
    total = 0
    for i in arr.items:
        total += i
    return total


def my_min(arr: List) -> int:
    """
    Функція для розрахування мінімального елементу списку.

    Аргументи:
        arr (List): Створенний список.

    Повертає:
        minimum (int): Мінімальне значення серед елементів списку.
    """
    iterator = iter(arr)
    try:
        minimum = next(iterator)
    except:
        raise ValueError("Empty sequence!")
    for i in arr:
        if i < minimum:
            minimum = i
    return minimum


def test_custom_len():
    """
    Тестування функції my_len()
    """
    my_list = List(1, 2, 3, 4, 5)
    assert my_len(my_list) == 5, f"Expected 5, got {my_len(my_list)}"
    my_empty_list = List()
    assert my_len(my_empty_list) == 0, f"Expected 5, got {my_len(my_list)}"
    print("my_len() passed!")


def test_custom_sum():
    """
    Тестування функції my_sum()
    """
    my_list = List(1, 2, 3, 4, 5)
    assert my_sum(my_list) == 15, f"Expected 15, got {my_sum(my_list)}"
    my_empty_list = List()
    assert my_sum(my_empty_list) == 0, f"Expected 5, got {my_sum(my_list)}"
    print("my_sum() passed!")


def test_custom_min():
    """
    Тестування функції my_min()
    """
    my_list = List(1, 2, 3, 4, 5)
    assert my_min(my_list) == 1, f"Expected 1, got {my_min(my_list)}"
    my_empty_list = List()
    try:
        my_min(my_empty_list)
    except ValueError as error:
        assert str(error) == "Empty sequence!", f"Unexpected error message: {str(error)}"
    print("my_min() passed!")


test_custom_len()
test_custom_sum()
test_custom_min()
