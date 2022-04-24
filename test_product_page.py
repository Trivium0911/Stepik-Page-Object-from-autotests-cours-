import pytest
from .pages.locators import LinksLocators
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


class TestGuestAddToBasketFromProductPage:

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = LinksLocators.PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()

    def test_guest_cant_see_success_message(self, browser):
        link = LinksLocators.PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.xfail(reason="Success message is presented, but should not be")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Success message is not disappeared")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.should_be_dissapered_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_quest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = LinksLocators.PRODUCT_PAGE
    page = BasketPage(browser, link)
    page.open()
    page.open_basket_page_from_product()
    page.should_be_empty_basket()
    page.should_be_messege_of_empty_basket()

@pytest.mark.logged_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LinksLocators.LOGIN_PAGE
        self.browser = browser
        page = LoginPage(browser, link)
        page.open()
        email, password = page.make_email_and_pass()
        page.register_new_user(email, password)
        page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = LinksLocators.PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = LinksLocators.PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()

@pytest.mark.need_review
def test_quest_can_go_to_login_page_from_product_page(browser):
    link = LinksLocators.MAIN_PAGE
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()