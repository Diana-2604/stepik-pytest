from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_product_name()
        self.should_be_product_price()
        self.should_be_add_to_cart_button()
        self.should_be_cart_total()
        self.should_be_cart_preview()
        self.should_be_added_to_cart_when_press_button()
        self.should_be_correct_product_name()
        self.should_be_correct_cart_total()

    def should_be_product_url(self):
        assert "?promo=newYear" in self.browser.current_url

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart button is not presented"

    def should_be_added_to_cart_when_press_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        assert "success message"

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert product_name.text in success_message.text, "Incorrect product name in success message"

    def should_be_correct_cart_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        info_message = self.browser.find_element(*ProductPageLocators.INFO_MESSAGE)
        assert product_price.text in info_message.text, "Incorrect cart total in success message"
