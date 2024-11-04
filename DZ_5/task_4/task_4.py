from typing import Generator


def file_generator(file_path: str, key_word: str = '') -> Generator[str]:
    """
    Функція генератор, який зчитує рядки з файлу, виводить тільки рядки з ключовим словом і записує їх у файл.
    :param file_path: Шлях до файлу з якого будемо зчитувати.
    :param key_word: Ключове слово за яким будемо шукати рядки.
    """
    index = 0
    with open(file_path, "r", encoding='UTF-8') as file:
        lines = file.readlines()
    with open('new_task_4_text', 'w', encoding='UTF-8') as file:
        while True:
            if index >= len(lines):
                break
            elif key_word in lines[index]:
                file.write(lines[index])
                yield lines[index]
                index += 1
            else:
                index += 1


if __name__ == "__main__":
    file_path = 'task_4_text'
    key_word = 'INFO'
    my_generator = file_generator(file_path, key_word)
    for line in my_generator:
        print(line)
