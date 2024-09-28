def create_user_settings():
    """Функція для створення налаштувань"""
    settings = {
        "theme": "Світла",
        "language": "Українська",
        "notifications": "Увімкнені"
    }

    def get_settings():
        """Вкладена функція для повертання налаштувань"""
        return f"Поточні налаштування користувача:" \
               f"\nТема: {settings['theme']},\nМова: {settings['language']} \nПовідомлення: {settings['notifications']}"

    def edit_settings(setting, value):
        """Вкладена функція для зміни значень налаштувань"""
        if setting in settings:
            print(f"Налаштування {setting} змінено на {value}")
        else:
            print("Невідоме налаштування!")

    return get_settings, edit_settings


get_settings, edit_settings = create_user_settings()
print(get_settings())
edit_settings("theme", "Темна")
