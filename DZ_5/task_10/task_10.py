import zipfile
import os


class ArchiveManager:
    """
    Контекстний менеджер для архівування файлів з заданої директорії.
    """
    def __init__(self, directory_path: str):
        """
        Ініціалізація екземпляра класу, створення списку з назвами файлів.
        :param directory_path: Шлях до директорії з файлами.
        """
        self.directory_path = directory_path
        self.files = os.listdir(directory_path)

    def __enter__(self):
        """
        Створюємо архів та додаємо туди кожний файл з директорії.
        """
        self.zip_file = zipfile.ZipFile(f'{os.path.basename(self.directory_path)}.zip', 'w', compression=zipfile.ZIP_DEFLATED)
        for file in self.files:
            add_file = os.path.join(self.directory_path, file)
            self.zip_file.write(add_file)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Обробляє завершення роботи з файлами і закриваємо архів, якщо він відкритий.
        """
        if self.zip_file:
            self.zip_file.close()


if __name__ == "__main__":
    path = 'task_10_files'
    with ArchiveManager(path) as directory:
        print("Архів створено!")  # Архів створено!
        print("Файли додано!")  # Файли додано!
    print("Архів закрито!")  # Архів закрито!

