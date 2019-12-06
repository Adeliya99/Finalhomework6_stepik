from .base_page import BasePage
from .locators import BasketPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_basket_url()
        self.should_be_go_to_registration_button()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "It is not basket page"

    def should_be_go_to_registration_button(self):
        assert self.is_element_present(*BasketPageLocators.GO_TO_REGISTRATION_BUTTON)
