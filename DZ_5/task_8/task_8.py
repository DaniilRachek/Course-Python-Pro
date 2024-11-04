import json


class ConfigManager:
    """
    Контекстний менеджер для роботи з конфігураційними файлами JSON.
    """
    def __init__(self, file_path: str):
        """
        Ініціалізація екземпляра класу.
        :param file_path: Шлях до JSON файлу.
        """
        self.file_path = file_path
        self.config_data = None

    def __enter__(self):
        """
        Відкриває конфігураційний файл JSON та зчитує з нього інформацію.
        :return: Інформація зчитана з конфігураційного файлу.
        """
        with open(self.file_path, 'r', encoding='UTF-8') as file:
            self.config_data = json.load(file)
        return self.config_data

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Записує дані в конфігураційний файл JSON при виході з нього.
        """
        with open(self.file_path, 'w', encoding='UTF-8') as file:
            json.dump(self.config_data, file)


if __name__ == "__main__":
    file_congig = 'config.json'

    with ConfigManager(file_congig) as config:
        print(f"Поточна конфігурація: {config}")  # Поточна конфігурація: {'setting1': 'initial_value', 'setting2': 123,
        # 'nested': {'key': 'initial_nested_value'}}

        config['new_setting'] = "new_value"
        print(f"Поточна конфігурація: {config}")  # Поточна конфігурація: {'setting1': 'initial_value', 'setting2': 123,
        # 'nested': {'key': 'initial_nested_value'}, 'new_setting': 'new_value'}
