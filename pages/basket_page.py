from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_HIDDEN_NOT_EMPTY_TITLE), \
            "Basket should be empty, but it's not"

    def should_be_messege_of_empty_basket(self):
        empty_message = self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTY).text
        message = "Ваша корзина пуста"
        assert message in empty_message, "No message about empty basket"