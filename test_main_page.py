from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


# Команда для запуска: pytest -v --tb=line --language=en test_main_page.py
# В этой команде мы использовали опцию PyTest --tb=line,
# которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста.
# Так вам будет проще разобраться в том, как выглядят сообщения об ошибках.
