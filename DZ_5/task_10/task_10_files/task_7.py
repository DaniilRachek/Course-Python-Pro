total_expense = 0  # змінна для загальних витрат


def add_expense(additional_expense):
    """Функція, яка додає витрати до загальних витрат"""
    global total_expense
    total_expense += additional_expense
    return f"Сума {additional_expense} гривень успішно додана до ваших витрат!"


def get_expense():
    """Функція для виведення загальних витрат"""
    return f"Загальна сума ваших витрат складає: {total_expense}"


def interface():
    """Функція для створення користувацького інтерфейсу"""
    print("Добрий день, вас вітає програма для відслідковування ваших витрат :)")
    menu()
    while True:
        if input("Бажаєте продовжити?").lower() == "так":
            menu()
        else:
            print("До побачення!")
            break


def menu():
    """Функція для виведення меню у користувацьому інтерфейсі"""
    print()
    while True:
        answer = input('Якщо ви бажаєте додати витрати введіть "1", якщо ж хочете переглянути витрати введіть "2":')
        if answer == "1":
            expense = input("Введіть суму витрати яку, хочете додати:")
            print(add_expense(int(expense)))
            break
        elif answer == "2":
            print(get_expense())
            break
        else:
            print("Введене некоректне значення!")
            print()


interface()
