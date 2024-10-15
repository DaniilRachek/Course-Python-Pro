class BinaryNumber:
    """
    Клас для представлення двійкового числа.

    Атрибути:
        num (int) : Десяткове число, яке ми перетворимо на двійкове
    """
    def __init__(self, num):
        self.num = num

    def __or__(self, other):
        """
        Проводить побітову операцію OR з двома двійковими числами.

        Аргументи:
            other (BinaryNumber) : Інше число, з яким проводиться операція.

        Повертає:
            BinaryNumber : Двійкове число з операцією OR
        """
        return BinaryNumber(self.num | other.num)

    def __and__(self, other):
        """
        Проводить побітову операцію AND з двома двійковими числами.

        Аргументи:
            other (BinaryNumber) : Інше число, з яким проводиться операція.

        Повертає:
            BinaryNumber : Двійкове число з операцією AND
        """
        return BinaryNumber(self.num & other.num)

    def __xor__(self, other):
        """
        Проводить побітову операцію XOR з двома двійковими числами.

        Аргументи:
            other (BinaryNumber) : Інше число, з яким проводиться операція.

        Повертає:
            BinaryNumber : Двійкове число з операцією XOR
        """
        return BinaryNumber(self.num ^ other.num)

    def __invert__(self):
        """
        Проводить побітову операцію NOT з двома двійковими числами.

        Повертає:
            BinaryNumber : Двійкове число з операцією NOT
        """
        num_bits = len(bin(self.num)) - 2
        mask = (1 << num_bits) - 1
        return BinaryNumber(~self.num & mask)

    def __str__(self):
        """
        Повертає двійкове представлення числа без префіксу '0b'.

        Повертає:
            str: Рядок з двійковим представленням числа.
        """
        return bin(self.num)[2:]


def test_binary_operations():
    """
    Тестування методів класу BinaryNumber
    """
    my_bin1 = BinaryNumber(5)
    my_bin2 = BinaryNumber(7)
    assert str(my_bin1 & my_bin2) == "101", f"AND test failed: {my_bin1} & {my_bin2} != 101"

    assert str(my_bin1 | my_bin2) == "111", f"OR test failed: {my_bin1} | {my_bin2} != 111"

    assert str(my_bin1 ^ my_bin2) == "10", f"XOR test failed: {my_bin1} ^ {my_bin2} != 010"

    assert str(~my_bin1) == "10", f"NOT test failed: ~{my_bin1} != 10"


test_binary_operations()
