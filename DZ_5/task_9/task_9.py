import shutil


class BackupManager:
    """
    Контекстний менеджер для резервного копіювання файлу.
    """
    def __init__(self, file_path: str):
        """
        Ініціалізація екземпляру класу.
        :param file_path: Шлях до файлу.
        """
        self.file_path = file_path
        self.backup_path = f'{file_path}_backup'

    def __enter__(self):
        """
        Створює резервну копію перед обробкою.
        :return: Шлях до оригінального файлу.
        """
        shutil.copy(self.file_path, self.backup_path)
        return self.file_path

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Обробляє завершення роботи з файлом
        - якщо виникла помилка, файл замінюється резервною копією.
        """
        if exc_type:
            shutil.copy(self.backup_path, self.file_path)


if __name__ == "__main__":
    file_path = 'task_9_text'

    # with BackupManager(file_path) as file:
    #     with open(file, "w", encoding="UTF-8") as f:
    #         f.write("Нова інформація у файлі")

    with BackupManager(file_path) as file:
        with open(file, "w", encoding="UTF-8") as f:
            f.write("Нова інформація у файлі")
            raise Exception
