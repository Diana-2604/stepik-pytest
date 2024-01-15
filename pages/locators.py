from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    HEADING = (By.CSS_SELECTOR, ".page-header > h1")
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//li[@class='active']")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1) > .alertinner > strong")
    INFO_MESSAGE = (By.CSS_SELECTOR, ".alert-info > .alertinner > p:nth-child(1) > strong")
