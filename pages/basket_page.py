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

    def open_basket_page_from_main(self):
        return self.go_to_basket_page_from(*BasketPageLocators.BASKET_LINK_FROM_MAIN)

    def open_basket_page_from_product(self):
        return self.go_to_basket_page_from(*BasketPageLocators.BASKET_LINK_FROM_PRODUCT)