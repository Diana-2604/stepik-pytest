from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_empty()
        self.should_not_be_empty()
        self.should_contain_text_if_empty()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Incorrect url"

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty, but should be"

    def should_not_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is empty, but shouldn't be"

    def should_contain_text_if_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), "Text is missing, but shouldn't be"

    def should_not_contain_text_if_has_items(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_TEXT), "Text is present, but shouldn't be"
