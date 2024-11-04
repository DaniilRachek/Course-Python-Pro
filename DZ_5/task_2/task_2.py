class IdIterator:
    """
    Ітератор, що генерує унікальні ідентифікатори для елементів списку.
    """
    def __init__(self, data: list):
        """
        Ініціалізує об'єкт IdIterator з заданим списком даних.
        :param data: Список, з якого буде створено ітератор.
        """
        self._data = data
        self._max_id = len(data)

    def __iter__(self):
        """
        Ініціалізує ітератор, скидає позицію до початку списку.
        :return: Сам об'єкт для ітерації.
        """
        self.position = 0
        return self

    def __next__(self):
        """
        Повертає наступний унікальний ідентифікатор для поточного елемента списку.
        :return: Унікальний хеш-ідентифікатор для поточного елемента.
        """
        if self.position >= self._max_id:
            raise StopIteration
        my_id = hash(self._data[self.position])
        self.position += 1
        return my_id


if __name__ == "__main__":
    datalist = ['a', 'g', 'e', '1']
    for id in IdIterator(datalist):
        print(id)
