import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_can_go_to_basket_page_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_contain_text_if_empty()

# Команда для запуска: pytest -v --tb=line --language=en test_main_page.py
# В этой команде мы использовали опцию PyTest --tb=line,
# которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста.
# Так вам будет проще разобраться в том, как выглядят сообщения об ошибках.
