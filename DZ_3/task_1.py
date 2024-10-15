class Fraction:
    """
    Клас для представлення дробового числа.

    Атрибути:
        numerator (int): Чисельник.
        denominator (int): Знаменник.
    """
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        """
        Додає два дроби.

        Якщо знаменники однакові, то додаються чисельники. Інакше дроби
        зводяться до спільного знаменника.

        Аргументи:
            other (Fraction) : Екземпляр дроби, який треба додати.

        Повертає:
            Fraction: Новий дріб, результат додавання.
        """
        if self.denominator == other.denominator:
            numerator = self.numerator + other.numerator
            denominator = self.denominator
        else:
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """
        Віднімає два дроби.

        Якщо знаменники однакові, то від першого чисельника віднімається другий.
        Інакше дроби зводяться до спільного знаменника.

        Аргументи:
            other (Fraction) : Екземпляр дроби, який треба відняти.

        Повертає:
            Fraction: Новий дріб, результат віднімання.
        """
        if self.denominator == other.denominator:
            numerator = self.numerator - other.numerator
            denominator = self.denominator
        else:
            numerator = self.numerator * other.denominator - other.numerator * self.denominator
            denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """
        Множить два дроба.

        Множить окремо 2 чисельники й 2 знаменники.

        Аргументи:
            other (Fraction) : Екземпляр дроби, який треба домножити.

        Повертає:
            Fraction: Новий дріб, результат множення.
        """
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        """
        Ділить два дроби.

        Множить чисельник першого на знаменник другого і
        чисельник другого на знаменник першого.

        Аргументи:
            other (Fraction) : Екземпляр дроби, на який треба поділити.

        Повертає:
            Fraction: Новий дріб, результат додавання.
        """
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"


frac1 = Fraction(8, 10)
frac2 = Fraction(2, 5)
print(frac1 + frac2)
print(frac1 - frac2)
print(frac1 * frac2)
print(frac1 / frac2)
