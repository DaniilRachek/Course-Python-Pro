discount = 0.1


def create_order(price, additional_discount):
    """Функція для розхрахунку ціни з урахуванням початкової знижки"""
    cost = price - (price * discount)

    def apply_additional_discount():
        """Вкладена функція для розрахунку ціни з урахуванням додаткових знижок"""
        nonlocal cost
        cost = price - (price * (discount + additional_discount))

    apply_additional_discount()

    return f"Початкова ціна {price}, кінцева ціна зі знижкою " \
           f"{int((discount + additional_discount) * 100)}%: {int(cost)}"


print(create_order(1000, 0.2))  # Початкова ціна 1000, кінцева ціна зі знижкою 30%: 700
print(create_order(5000, 0.06))  # Початкова ціна 5000, кінцева ціна зі знижкою 16%: 4200
