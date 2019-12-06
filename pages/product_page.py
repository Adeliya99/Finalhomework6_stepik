from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_add_to_basket_button()

    def should_be_product_url(self):
        assert 'catalogue' in self.browser.current_url

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Button form is not presented"

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def go_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.GO_TO_BASKET_BUTTON)
        basket_link.click()

    def should_be_empty_basket(self):
        basket_content = self.browser.find_element(*ProductPageLocators.BASKET_IN)
        assert "Your basket is empty" in basket_content.text, "Basket is not empty"

    def should_be_product_image(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IMAGE), "Product image is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"