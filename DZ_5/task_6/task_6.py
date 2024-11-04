import os


class FileIterator:
    """
    Клас для створення ітератора, який буде проходити по каталогу і повертати назву і розмір кожного файлу
    """
    def __init__(self, directory_path: str):
        """
        Ініціалізація екземпляра класу FileIterator
        :param directory_path: шлях до каталогу, у якому перебиратимемо файли.
        """
        self.directory = directory_path
        self.files = [f for f in os.listdir(directory_path) if os.path.isfile(f'{directory_path}/{f}')]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        Переходить на наступний файл.
        :return: Рядок з порядковим індексом, ім'ям та розміром файлу.
        """
        if self.index >= len(self.files):
            raise StopIteration

        file_path = '/'.join((self.directory, self.files[self.index]))
        filename = self.files[self.index]
        size = os.path.getsize(file_path)

        self.index += 1
        return f'{self.index}. {filename}, {size} bytes'


if __name__ == "__main__":
    path = 'files'
    file_iter = FileIterator(path)
    for file in file_iter:
        print(file)
