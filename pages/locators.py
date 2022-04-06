from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # tuple to be passed as args (how, what)


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")  # TODO: change selector value
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  # TODO: change selector value
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  # TODO: change selector value


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE = (By.CSS_SELECTOR, "div.product_main > h1")
    PRICE = (By.CSS_SELECTOR, "div.product_main > p")
    TITLE_CHECKED = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRICE_CHECKED = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
