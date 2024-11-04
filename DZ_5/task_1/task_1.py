class ReverseFile:
    """
    Клас для ітерації по рядках файлу у зворотному порядку.
    """
    def __init__(self, filename):
        """
        Ініціалізує об'єкт ReverseFile з заданим файлом.
        :param filename: Назва файлу.
        """
        self._filename = filename
        self.position = 0

    def __iter__(self):
        """
        Ініціалізує ітератор, відкриває файл та зчитує рядки у зворотному порядку.
        :return: Сам об'єкт для ітерації
        """
        with open(self._filename, 'r', encoding="UTF-8") as f:
            self.lines = f.readlines()[::-1]
        self.position = 0
        return self

    def __next__(self):
        """
        Повертає наступний рядок з файлу у зворотному порядку.
        :return: Наступний рядок з файлу у зворотному порядку.
        """
        if self.position >= len(self.lines):
            raise StopIteration
        current_position = self.position
        self.position += 1
        return self.lines[current_position].strip()


if __name__ == "__main__":
    file = ReverseFile('example')
    for line in file:
        print(line)

    file2 = ReverseFile('example2')
    for line in file2:
        print(line)
