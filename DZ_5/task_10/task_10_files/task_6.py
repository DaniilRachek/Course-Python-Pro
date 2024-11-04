def create_calculator(operator):
    """Функція для створення калькулятора, яка приймає значення оператора"""

    def add(first_number, second_number):
        """Функція для додавання чисел"""
        return f'{first_number} + {second_number} = {first_number + second_number}'

    def subtraction(first_number, second_number):
        """Функція для віднімання чисел"""
        return f'{first_number} - {second_number} = {first_number - second_number}'

    def multiplication(first_number, second_number):
        """Функція для множення чисел"""
        return f'{first_number} * {second_number} = {first_number * second_number}'

    def division(first_number, second_number):
        """Функція для ділення чисел"""
        return f'{first_number} / {second_number} = {first_number / second_number}'

    actions = {"+": add, "-": subtraction, "*": multiplication, "/": division}
    return actions[operator]


calculator1 = create_calculator("+")
print(calculator1(10, 15))
print(calculator1(12, 19))
calculator2 = create_calculator("*")
print(calculator2(5, 5))