import re


class User:
    """
    Клас для представлення користувача

    Атрибути:
        __first_name (str): Ім'я користувача.
        __last_name (str): Прізвище користувача.
        __email (str): Email користувача.
    """
    def __init__(self, first_name, last_name, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = self.check_email(email)

    @staticmethod
    def check_email(email: str) -> str:
        """
        Метод перевіряє коректність введеного email користувача.

        Аргументи:
            email (str): Email користувача

        Повертає:
            email (str): Email користувача
        """
        pattern = re.compile(r'\w+@\w+.\w')
        if pattern.search(email):
            return email
        else:
            raise ValueError("Invalid email adress value!")

    @property
    def first_name(self):
        """
        Повертає ім'я особи.

        Повертає:
            str: Ім'я особи.
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, new_first_name):
        """
        Встановлює нове ім'я для особи.

        Аргументи:
            new_first_name (str): Нове ім'я.
        """
        self.__first_name = new_first_name

    @property
    def last_name(self):
        """
        Повертає прізвище особи.

        Повертає:
            str: Прізвище особи.
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, new_last_name):
        """
        Встановлює нове прізвище для особи.

        Аргументи:
            new_last_name (str): Нове прізвище.
        """
        self.__last_name = new_last_name

    @property
    def email(self):
        """
        Повертає електронну пошту особи.

        Повертає:
            str: Електронна пошта особи.
        """
        return self.__email

    @email.setter
    def email(self, new_email):
        """
        Встановлює нову електронну пошту особи після перевірки.

        Аргументи:
            new_email (str): Нова електронна пошта.
        """
        self.__email = self.check_email(new_email)


my_user = User("Kyrylo", "Symonenko", "kyryl.symonenko@gmail.com")
print(my_user.first_name)
my_user.first_name = "Stepan"
print(my_user.first_name)
my_user.email = "kyryl.com"
