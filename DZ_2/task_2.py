subscribers = ["Микола", "Анатолій", "Олена"]


def subscribe(new_subscriber):
    """Функція для підписки людини за ім'ям """
    subscribers.append(new_subscriber)

    def confirm_subscription(subscribers_name):
        """Вкладена функція для сповіщення про підписку"""
        return f"Підписка підтверджена для {subscribers_name}"

    return confirm_subscription(new_subscriber)


def unsubscribe(subscriber):
    """Функція для відписки людини за ім'ям """
    subscribers.remove(subscriber)

    def confirm_unsubscribe(subscribers_name):
        """Вкладена функція для сповіщення про відписку"""
        return f"{subscribers_name} успішно відписаний"

    return confirm_unsubscribe(subscriber)


print(subscribers)
subscribe("Марія")
print(subscribers)
print(unsubscribe("Микола"))
print(subscribers)
