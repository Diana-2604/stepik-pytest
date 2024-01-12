# импорт базового класса BasePage
from .base_page import BasePage


# класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # Метод __init__ вызывается при создании объекта.
    # Конструктор выше с ключевым словом super на самом деле только
    # вызывает конструктор класса предка и передает ему все те аргументы,
    # которые мы передали в конструктор MainPage.
