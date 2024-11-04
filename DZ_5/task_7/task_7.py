import re


def error_log_generator(file_path: str):
    """
    Функція генератор, який зчитує рядки з файлу, виводить тільки рядки з кодом помилки і записує їх у файл.
    :param file_path: Шлях до файлу з якого будемо зчитувати.
    """
    error_pattern = re.compile(r'\s([45]\d{2})\s')
    with open(file_path, 'r', encoding="UTF-8") as file:
        for line in file:
            if error_pattern.search(line):
                yield line


if __name__ == "__main__":
    file_path = 'log_file'
    error_path = 'error_log'

    with open(error_path, 'w', encoding='UTF-8') as file:
        for error_line in error_log_generator(file_path):
            file.write(error_line)
            print(error_line)
