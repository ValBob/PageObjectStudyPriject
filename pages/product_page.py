from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_basket_content(self):
        assert self.title == self.browser.find_element(*ProductPageLocators.TITLE_CHECKED).text,\
            "Product title doesn't matched basket content"

    def should_be_correct_product_price(self):
        assert self.price == self.browser.find_element(*ProductPageLocators.PRICE_CHECKED).text,\
            "Product price doesn't matched basket price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS), \
            "Success message should disappear, but has not"
