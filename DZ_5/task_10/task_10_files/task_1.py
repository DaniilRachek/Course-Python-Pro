def my_sum(*args):
    """Кастомна функція для заміни вбудованої функції sum"""
    return "This is custom sum function!"


numbers = [10, 20, 30, 40]
print(sum(numbers))

sum = my_sum()

print(my_sum())
print(sum(numbers))