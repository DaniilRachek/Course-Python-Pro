events = []  # Список для подій


def calendar():
    """Функція, яка описує поведінку календаря"""

    def add_event(event):
        """Вкладена функція для додавання події у список"""
        events.append(event)
        print(f'Подію "{event}" додано до календаря.')

    def remove_event(event):
        """Вкладена функція для видалення події зі списку"""
        if event in events:
            events.remove(event)
            print(f'Подію "{event}" видалено з календаря.')
        else:
            print(f'Подія "{event}" відсутня у календарі')

    def view_events():
        """Функція для перегляду усіх подій у списку"""
        if events:
            print("\n" + "*" * 30)
            print("Події у календарі:")
            for number, event in enumerate(events, 1):
                print(f'{number}. {event}')
        else:
            print("Немає подій")

    return add_event, remove_event, view_events


add, remove, view = calendar()

add("Медична конференція о 10:30")
add("Обід о 13:00")
view()
remove("Медична конференція о 10:30")
view()

