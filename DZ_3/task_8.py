class Price:
    """
    Клас для представлення ціни товару.

    Атрибути:
        price (float): Значення ціни.
    """
    def __init__(self, price):
        self.price = float(price)

    def add_price(self, add_value):
        """
        Додає нове значення до ціни.

        Аргументи:
             add_value (int, float): Значення, яке додаємо.
        """
        self.price += add_value

    def sub_price(self, sub_value):
        """
        Віднімає нове значення від ціни.

        Аргументи:
             sub_value (int, float): Значення, яке віднімаємо.
        """
        self.price -= sub_value

    def __lt__(self, other):
        """
        Перевіряє чи перша ціна менша за другу.

        Аргументи:
            other (Vector) : Друга ціна, з якою порівнюємо.

        Повертає:
            bool: True, якщо перша ціна менше.
        """
        return self.price < other.price

    def __eq__(self, other):
        """
        Перевіряє чи перша ціна дорівнює другій.

        Аргументи:
            other (Vector) : Друга ціна, з якою порівнюємо.

        Повертає:
            bool: True, якщо ціни однакові.
        """
        return self.price == other.price

    def __gt__(self, other):
        """
        Перевіряє чи перша ціна більша за другу.

        Аргументи:
            other (Vector) : Друга ціна, з якою порівнюємо.

        Повертає:
            bool: True, якщо перша ціна більше.
        """
        return self.price > other.price

    def __str__(self):
        """
        Повертає строкове представлення ціни продукту
        з округленням до 2 знаків після коми.

        Повертає:
            str: Представлення ціни продукту.
        """
        return f"The price of product is {self.price:.2f}"


my_price1 = Price(12)
my_price2 = Price(117)

my_price1.add_price(15)
print(my_price1)

my_price1.sub_price(10)
print(my_price1)

print(my_price1 > my_price2)

