from typing import Generator


def num_generator(max_count: int, file_path='task_5_text') -> Generator[int]:
    """
    Функція генератор для створення послідовності з парних чисел зазначеної довжини,
    виведення цих чисел та запис їх у файл.
    :param max_count: Кількість чисел у послідовності.
    :param file_path: Шлях до файлу, у який записуватемо нашу послідовність чисел.
    :return:
    """
    n = 0
    index = 0
    with open(file_path, 'w', encoding='UTF-8') as file:
        while index <= max_count:
            yield n
            file.write(str(n) + ' ')
            n += 2
            index += 1


if __name__ == "__main__":
    my_generator = num_generator(100)
    try:
        while True:
            print(next(my_generator))
    except StopIteration:
        pass
