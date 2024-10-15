class Vector:
    """
    Клас для представлення вектора.

    Атрибути:
        coordinates (tuple): Координати x та y вектора.
    """

    def __init__(self, coordinates):
        self.first_coordinate = coordinates[0]
        self.second_coordinate = coordinates[1]
        self.length = self.calculate_length()

    def calculate_length(self):
        """
        Розраховує довжину вектора за координатами.

        Повертає:
            length (float): Довжина вектора.
        """
        length = round((self.first_coordinate ** 2 + self.second_coordinate ** 2) ** 0.5, 2)
        return length

    def __add__(self, other):
        """
        Додає координати двох векторів.

        Аргументи:
            other (Vector) : Другий вектор, який додаємо.

        Повертає:
            Vector : Новий вектор, результат додавання.
        """
        first_coordinate = (self.first_coordinate + other.first_coordinate)
        second_coordinate = (self.second_coordinate + other.second_coordinate)
        return Vector((first_coordinate, second_coordinate))

    def __sub__(self, other):
        """
        Віднімає координати двох векторів.

        Аргументи:
            other (Vector) : Другий вектор, який віднімаємо.

        Повертає:
            Vector : Новий вектор, результат віднімання.
        """
        first_coordinate = (self.first_coordinate - other.first_coordinate)
        second_coordinate = (self.second_coordinate - other.second_coordinate)
        return Vector((first_coordinate, second_coordinate))

    def __mul__(self, number):
        """
        Множить вектор на число.

        Аргументи:
            number (int): Число на яке множимо вектор.

        Повертає:
            Vector : Новий вектор, результат множення.
        """
        return Vector((self.first_coordinate * number, self.second_coordinate * number))

    def __lt__(self, other):
        """
        Перевіряє чи довжина першого вектора менша за довжину другого.

        Аргументи:
            other (Vector) : Другий вектор, з яким порівнюємо.

        Повертає:
            bool: Більше чи менше перший вектор.
        """
        return self.length < other.length

    def __gt__(self, other):
        """
        Перевіряє чи довжина першого вектора більша за довжину другого.

        Аргументи:
            other (Vector) : Другий вектор, з яким порівнюємо.

        Повертає:
            bool: Більше чи менше перший вектор.
        """
        return self.length > other.length

    def __eq__(self, other):
        """
        Перевіряє чи довжина першого вектора дорівнює довжині другого.

        Аргументи:
            other (Vector) : Другий вектор, з яким порівнюємо.

        Повертає:
            bool: Чи дорівнюють вектори.
        """
        return self.length == other.length

    def __str__(self):
        """
        Повертає строкове представлення вектора з координатами.
        й довжиною

        Повертає:
            str : Строкове представлення вектора з координатами
            й довжиною
        """
        return f"Vector with coordinates ({self.first_coordinate}, {self.second_coordinate}) " \
               f"and length {self.length}"


my_vector1 = Vector((1, 2))
my_vector2 = Vector((2, 2))
print(my_vector1 + my_vector2)
print(my_vector1 - my_vector2)
print(my_vector1 * 3)
print(my_vector1 < my_vector2)
print(my_vector1 > my_vector2)
print(my_vector1 == my_vector2)
