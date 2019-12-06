from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket(self):
        basket_link = self.browser.find_element(*MainPageLocators.GO_TO_BASKET_BUTTON)
        basket_link.click()

    def should_be_empty_basket(self):
        basket_content = self.browser.find_element(*MainPageLocators.BASKET_IN)
        assert "Your basket is empty" in basket_content.text, "Basket is not empty"

    def should_be_find(self):
        assert self.browser.find_element(*MainPageLocators.FIND_BUTTON), "Find button is not presented"

    def find_product(self):
        find_input = self.browser.find_element(*MainPageLocators.FIND_INPUT)
        find_input.send_keys("Coders at Work")
        find = self.browser.find_element(*MainPageLocators.FIND_BUTTON)
        find.click()

    def should_be_product_page(self):
        assert self.browser.find_element(*ProductPageLocators.FOUNDED_PRODUCT), "It is not product page"


