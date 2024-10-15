class Vector:
    """
    Клас для представлення n-вимірного вектора

    Атрибути:
        coordinates (tuple): Координати вектора.
        dimension (int): Кількість вимірів вектора.
        length (float): довжина вектора.
    """
    def __init__(self, *args):
        self.coordinates = args
        self.dimension = len(args)
        self.length = self.calculate_length()

    def calculate_length(self):
        """
        Розраховує довжину вектора за координатами.

        Повертає:
            length (float): Довжина вектора.
        """
        length = 0
        for x in self.coordinates:
            length += x**2
        return round(length**0.5, 2)

    def __add__(self, other):
        """
        Додає два вектори, якщо вони мають однакову кількість вимірів.

        Аргументи:
            other (Vector): Інший вектор, який додаємо.

        Повертає:
            Vector: Новий вектор, який є сумою двох векторів.
            str: Повідомлення, якщо вектори мають різну кількість вимірів.
        """
        if self.dimension == other.dimension:
            new_coordinates = []
            for a, b in zip(self.coordinates, other.coordinates):
                new_coordinates.append(a + b)
            return Vector(*new_coordinates)
        else:
            return f"Cannot add! Vectors have different dimensions"

    def __sub__(self, other):
        """
        Віднімає один вектор від іншого, якщо вони мають однакову кількість вимірів.

        Аргументи:
            other (Vector): Інший вектор, який віднімаємо.

        Повертає:
            Vector: Новий вектор, який є різницею двох векторів.
            str: Повідомлення, якщо вектори мають різну кількість вимірів.
        """
        if self.dimension == other.dimension:
            new_coordinates = []
            for a, b in zip(self.coordinates, other.coordinates):
                new_coordinates.append(a - b)
            return Vector(*new_coordinates)
        else:
            return f"Subtraction is impossible! Vectors have different dimensions"

    def __mul__(self, other):
        """
         Розраховує скалярний добуток двох векторів, якщо
         вони мають однакову кількість вимірів.

        Аргументи:
            other (Vector): Інший вектор, який множимо.

        Повертає:
            str: Повідомлення про отриманий скалярний добуток.
            str: Повідомлення, якщо вектори мають різну кількість вимірів.
        """
        if self.dimension == other.dimension:
            result = 0
            for a, b in zip(self.coordinates, other.coordinates):
                result += a * b
            return f"Scalar product is {result}"
        else:
            return f"It is impossible to find the scalar product! Vectors have different dimensions"

    def __lt__(self, other):
        """
        Перевіряє чи довжина першого вектора менша за довжину другого.

        Аргументи:
            other (Vector) : Другий вектор, з яким порівнюємо.

        Повертає:
            bool: True, якщо перший вектор менше.
        """
        return self.length < other.length

    def __eq__(self, other):
        """
        Перевіряє чи довжина першого вектора дорівнює довжині другого.

        Аргументи:
            other (Vector) : Другий вектор, з яким порівнюємо.

        Повертає:
            bool: True, якщо довжина векторів рівна.
        """
        return self.length == other.length

    def __gt__(self, other):
        """
        Перевіряє чи довжина першого вектора більша за довжину другого.

        Аргументи:
            other (Vector) : Другий вектор, з яким порівнюємо.

        Повертає:
            bool: True, якщо перший вектор більше.
        """
        return self.length > other.length

    def __str__(self):
        """
        Повертає рядкове представлення вектора, вказуючи координати і довжину.

        Повертає:
            str: Представлення вектора.
        """
        return f"Vector with coordinates {self.coordinates} and length {self.length}"


my_vector1 = Vector(1, 2, 3)
my_vector2 = Vector(2, 3, 4)
print(my_vector1 + my_vector2)
print(my_vector1 - my_vector2)
print(my_vector1 * my_vector2)
print(my_vector1 < my_vector2)
print(my_vector1 == my_vector2)
print(my_vector1 > my_vector2)
