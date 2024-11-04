import os
import csv
from PIL import Image


class ImageIterator:
    """
    Клас для ітерування по каталогу з зображеннями
    """

    def __init__(self, directory_path, csv_file='image_metadata.csv'):
        """
        Ініціалізує екземпляр класу ImageIterator і записує заголовки у створений csv-файл
        :param directory_path: Шлях до директорії з зображеннями.
        :param csv_file: Назва сsv-файлу, у який ми записуватемо метадані зображень.
        """
        self.directory = directory_path
        self.csv_file = csv_file
        self.image_files = [file for file in os.listdir(directory) if file.endswith(('png', 'jpg', 'jpeg'))]
        self.index = 0

        with open(self.csv_file, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["Filename", "Format", "Width", "Height", "Mode"])

    def __iter__(self):
        return self

    def __next__(self):
        """
        Відкриває наступне зображення, витягує його метадані, зберегає їх у csv-файл та виводить їх.
        :return: Метадані зображення.
        """
        if self.index >= len(self.image_files):
            raise StopIteration

        image_path = os.path.join(self.directory, self.image_files[self.index])
        with Image.open(image_path) as img:
            metadata = {
                'Filename': self.image_files[self.index],
                'Format': img.format,
                'Width': img.width,
                'Height': img.height,
                'Mode': img.mode
                }
        with open(self.csv_file, 'a') as file:
            writer = csv.writer(file)
            writer.writerow((metadata['Filename'], metadata['Format'], metadata['Width'], metadata['Height'],
                             metadata['Mode']))

        self.index += 1
        return metadata


if __name__ == "__main__":
    directory = "images"
    iterator = ImageIterator(directory)

    for image_metadata in iterator:
        print(image_metadata)
