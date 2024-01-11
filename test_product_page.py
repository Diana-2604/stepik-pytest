import pytest

from pages.product_page import ProductPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


# def test_guest_can_see_product_page(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_product_url()
#     page.should_be_product_name()
#     page.should_be_product_price()

@pytest.mark.parametrize('number', ["0", "1", "2", "3", "4", "5", "6",
                                    pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.should_be_added_to_cart_when_press_button()
    page.should_be_correct_product_name()
    page.should_be_correct_cart_total()

# Чтобы увидеть проверочный код в консоли, запускайте PyTest с параметром -s:
# pytest -s test_product_page.py
