from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators, BasketPageLocators
import time
import pytest


@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    email = str(time.time()) + "@fakemail.org"
    password = "stepikpassword123"
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_page()
    page.register_new_user(email, password)
    page = BasePage(browser, browser.current_url)
    page.should_be_authorized_user()
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.need_review
@pytest.mark.need_review_custom_scenarios
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
    page.is_not_element_present(*BasketPageLocators.GO_TO_REGISTRATION_BUTTON)


@pytest.mark.need_review_custom_scenarios
def test_guest_can_see_the_product_image(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_be_product_image()


@pytest.mark.need_review_custom_scenarios
def test_guest_can_see_the_product_price(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_be_product_price()