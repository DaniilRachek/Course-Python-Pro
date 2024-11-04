def edit_price_decorator(new_price):
    """Функція-декоратор для зміни ціни товара"""
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            product_price_func = func(*args, **kwargs)
            return product_price_func(new_price)
        return wrapper
    return my_decorator


@edit_price_decorator(10)
def create_product(title):
    """Функція для створення товару"""
    def product_price(price):

        def product_amount(amount):
            print(f"Product: {title}, Price: {price}, Amount: {amount}")
        return product_amount
    return product_price


my_product = create_product("bread")
my_product(20)
