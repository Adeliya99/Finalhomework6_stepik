from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "[class = 'btn-group']")
    BASKET_IN = (By.CSS_SELECTOR, "#content_inner")
    FIND_INPUT = (By.CSS_SELECTOR, "#id_q")
    FIND_BUTTON = (By.CSS_SELECTOR, "input[type = 'submit']")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name = registration_submit]")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "[class = 'btn-group']")
    BASKET_IN = (By.CSS_SELECTOR, "#content_inner")
    FOUNDED_PRODUCT = (By.CSS_SELECTOR, "#id_sort_by")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".item.active")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[class = 'col-sm-6 product_main'] p.price_color")


class BasketPageLocators():
    GO_TO_REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[class = 'btn btn-lg btn-primary btn-block']")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "[class = 'btn-group']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
