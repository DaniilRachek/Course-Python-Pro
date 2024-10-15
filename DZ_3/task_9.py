class ProductWithGetSet:
    """
    Клас для представлення продуктами з гетерами й сетерами.

    Атрибути:
         name (str): Назва продукту.
         price (int, float): Ціна продукту.
    """
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def get_price(self):
        """
        Повертає значення ціни.

        Повертає:
            _price (int, float): Ціна продукту.
        """
        return self._price

    def set_price(self, new_price):
        """
        Встановлює нове значення ціни.

        Аргументи:
            new_price (int, float): Нова ціна
        """
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError("Value must be positive!")


class ProductWithProperty:
    """
    Клас для представлення продуктами з @property.

    Атрибути:
         name (str): Назва продукту.
         price (int, float): Ціна продукту.
    """
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        """
        Повертає значення ціни.

        Повертає:
            _price (int, float): Ціна продукту.
        """
        return self._price

    @price.setter
    def price(self, new_price):
        """
        Встановлює нове значення ціни.

        Аргументи:
            new_price (int, float): Нова ціна
        """
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError("Value must be positive!")


class PriceDescriptor:
    """
    Дескриптор для управління атрибутом _price.
    """
    def __get__(self, instance, owner):
        """
        Повертає значення ціни.

        Повертає:
            _price (int, float): Ціна продукту.
        """
        return instance._price

    def __set__(self, instance, value):
        """
        Встановлює нове значення ціни.

        Аргументи:
            value (int, float): Нова ціна
        """
        if value >= 0:
            instance._price = value
        else:
            raise ValueError("Value must be positive!")


class ProductWithDescriptor:
    """
    Клас для представлення продуктами з дескриптором.

    Атрибути:
         name (str): Назва продукту.
         price (int, float): Ціна продукту.
    """
    price = PriceDescriptor()

    def __init__(self, name, price):
        self.name = name
        self._price = price


def test_get_set():
    """
    Тестування методів класу ProductWithGetSet.
    """
    my_product = ProductWithGetSet("milk", 10)
    assert my_product.get_price() == 10, f"Expected 10, got {my_product.get_price()}"

    my_product.set_price(6)
    assert my_product.get_price() == 6, f"Expected 6, got {my_product.get_price()}"

    try:
        my_product.set_price(-1)
    except ValueError as error:
        assert str(error) == "Value must be positive!", f"Unexpected error message: {str(error)}"

    print("ProductWithGetSet passed!")


def test_property():
    """
    Тестування методів класу ProductWithGetSet.
    """
    my_product = ProductWithProperty("milk", 10)
    assert my_product.price == 10, f"Expected 10, got {my_product.price}"

    my_product.price = 6
    assert my_product.price == 6, f"Expected 6, got {my_product.price}"

    try:
        my_product.price = -1
    except ValueError as error:
        assert str(error) == "Value must be positive!", f"Unexpected error message: {str(error)}"

    print("ProductWithProperty passed!")


def test_descriptor():
    """
    Тестування методів класу ProductWithGetSet.
    """
    my_product = ProductWithDescriptor("milk", 10)
    assert my_product.price == 10, f"Expected 10, got {my_product.price}"

    my_product.price = 6
    assert my_product.price == 6, f"Expected 6, got {my_product.price}"

    try:
        my_product.price = -1
    except ValueError as error:
        assert str(error) == "Value must be positive!", f"Unexpected error message: {str(error)}"

    print("ProductWithDescriptor passed!")


test_get_set()
test_property()
test_descriptor()
