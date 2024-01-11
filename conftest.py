# Для хранения часто употребимых фикстур и хранения глобальных настроек нужно использовать
# файл conftest.py, который должен лежать в директории верхнего уровня в вашем проекте с тестами.
# Можно создавать дополнительные файлы conftest.py в других директориях,
# но тогда настройки в этих файлах будут применяться только к тестам в под-директориях.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

supported_browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: en / ru / es / fr")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    if browser_name in supported_browsers:
        if browser_name == "chrome":
            browser = webdriver.Chrome(options=options)
            browser.maximize_window()
            print(f"\nstart {browser_name} browser for test..")
        elif browser_name == "firefox":
            browser = webdriver.Firefox(options=options_firefox)
            browser.maximize_window()
            print(f"\nstart {browser_name} browser for test..")
    else:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")

    yield browser
    print("\nquit browser..")
    browser.quit()
