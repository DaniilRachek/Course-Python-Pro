from random import randint
default_time = 60  # Початкове значення часу раунда тренування


def training_session(training_rounds):
    """Функція, яка приймає кількість раундів тренування і виводить час кожного з них"""
    time_per_round = default_time

    def adjust_time(time):
        """Вкладена функція для зміни значення часу раунду на випадкове"""
        nonlocal time_per_round
        time_per_round = time

    for number_of_round in range(1, training_rounds + 1):
        print(f"Раунд {number_of_round}: {time_per_round} хвилин")
        adjust_time(randint(20, 61))


training_session(3)
print("*" * 60)
training_session(7)
