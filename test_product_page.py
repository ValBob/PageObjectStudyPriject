import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


# @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# def test_guest_can_add_product_to_basket(browser, num):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
#     print(f'item {num} is testing')
#     page = ProductPage(browser, link)
#     page.open()
#     page.title = page.browser.find_element(*ProductPageLocators.TITLE).text
#     page.price = page.browser.find_element(*ProductPageLocators.PRICE).text
#     page.add_product_to_basket()
#     page.should_be_correct_basket_content()
#     page.should_be_correct_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # open product page
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # add product to basket
    page.add_product_to_basket()
    # check with is_not_element_present
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # open product page
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # check with is_not_element_present
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # open product page
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # add product to basket
    page.add_product_to_basket()
    # check with is_disappeared
    page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, page.url)  # rewrite page as BasketPage instance
    page.should_not_be_product_in_basket()
    page.should_be_message_about_empty_basket()


