import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


@pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_guest_can_add_product_to_basket(browser, num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    print(f'item {num} is testing')
    page = ProductPage(browser, link)
    page.open()
    page.title = page.browser.find_element(*ProductPageLocators.TITLE).text
    page.price = page.browser.find_element(*ProductPageLocators.PRICE).text
    page.add_product_to_basket()
    page.should_be_correct_basket_content()
    page.should_be_correct_product_price()
