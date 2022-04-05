from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # tuple to be passed as args (how, what)


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")  # TODO: change selector value
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  # TODO: change selector value
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  # TODO: change selector value


